import os
import re
import time

from web3 import Web3

from dydx3 import Client
from dydx3 import constants
# from dydx3 import DydxApiError
from dydx3 import epoch_seconds_to_iso
from dydx3 import generate_private_key_hex_unsafe

from tests.constants import DEFAULT_HOST
from tests.constants import DEFAULT_NETWORK_ID
# from tests.constants import SEVEN_DAYS_S

from integration_tests.util import wait_for_condition

HOST = os.environ.get('V3_API_HOST', DEFAULT_HOST)
NETWORK_ID = os.environ.get('NETWORK_ID', DEFAULT_NETWORK_ID)

source_private_key = os.environ.get('TEST_SOURCE_PRIVATE_KEY')
if source_private_key is None:
    raise ValueError('TEST_SOURCE_PRIVATE_KEY must be set')

web3_provider = os.environ.get('TEST_WEB3_PROVIDER_URL')
if web3_provider is None:
    raise ValueError('TEST_WEB3_PROVIDER_URL must be set')

# Create client that will be used to fund the new user.
source_client = Client(
    host='',
    eth_private_key=source_private_key,
    web3_provider=web3_provider,
)

# Create an Ethereum account and STARK keys for the new user.
web3_account = Web3(None).eth.account.create()
ethereum_address = web3_account.address
eth_private_key = web3_account.key
stark_private_key = generate_private_key_hex_unsafe()

print("ethereum_address: ", ethereum_address)
print("eth_private_key: ", eth_private_key)
print("stark_private_key: ", stark_private_key)

# Fund the new user with ETH and USDC.
fund_eth_hash = source_client.eth.transfer_eth(
    to_address=ethereum_address,
    human_amount=0.001,
)
print('funding eth (hash %s)' % (fund_eth_hash, ))

fund_usdc_hash = source_client.eth.transfer_token(
    to_address=ethereum_address,
    human_amount=2,
)
print('funding usdc (hash %s)' % (fund_usdc_hash, ))

print('Waiting for funds...')
source_client.eth.wait_for_tx(fund_eth_hash)
source_client.eth.wait_for_tx(fund_usdc_hash)
print('...done.')

# Create client for the new user.
client = Client(
    host=HOST,
    network_id=NETWORK_ID,
    stark_private_key=stark_private_key,
    eth_private_key=eth_private_key,
    web3_provider=web3_provider,
)

# Onboard the user.
res = client.onboarding.create_user()
api_key_credentials = res['apiKey']

print('eth_private_key', eth_private_key)
print('stark_private_key', stark_private_key)
print('client.api_key_credentials', client.api_key_credentials)

# Get the user.
get_user_result = client.private.get_user()
assert get_user_result['user'] == {
    'ethereumAddress': ethereum_address.lower(),
    'isRegistered': False,
    'email': None,
    'username': None,
    'userData': {},
    'makerFeeRate': '0.0005',
    'takerFeeRate': '0.0015',
    'makerVolume30D': '0',
    'takerVolume30D': '0',
    'fees30D': '0',
}

# Get the registration signature.
registration_result = client.private.get_registration()
signature = registration_result['signature']
assert re.match('0x[0-9a-f]{130}$', signature) is not None, (
    'Invalid registration result: {}'.format(registration_result)
)

# Register the user on-chain.
registration_tx_hash = client.eth.register_user(signature)
print('Waiting for registration...')
client.eth.wait_for_tx(registration_tx_hash)
print('...done.')

# Set the user's username.
username = 'integration_user_{}'.format(int(time.time()))
client.private.update_user(username=username)

# Get the primary account.
get_account_result = client.private.get_account(
    ethereum_address=ethereum_address,
)
account = get_account_result['account']
assert int(account['starkKey'], 16) == int(client.stark_public_key, 16)

# Get all accounts.
get_all_accounts_result = client.private.get_accounts()
get_all_accounts_public_keys = [
    a['starkKey'] for a in get_all_accounts_result['accounts']
]
assert int(client.stark_public_key, 16) in [
    int(k, 16) for k in get_all_accounts_public_keys
]

# Get positions.
get_positions_result = client.private.get_positions(market='BTC-USD')
assert get_positions_result == {'positions': []}

# Set allowance on the Starkware perpetual contract, for the deposit.
approve_tx_hash = client.eth.set_token_max_allowance(
    client.eth.get_exchange_contract().address,
)
print('Waiting for allowance...')
client.eth.wait_for_tx(approve_tx_hash)
print('...done.')

# Send an on-chain deposit.
deposit_tx_hash = client.eth.deposit_to_exchange(
    account['positionId'],
    3,
)
print('Waiting for deposit...')
client.eth.wait_for_tx(deposit_tx_hash)
print('...done.')

# Wait for the deposit to be processed.
print('Waiting for deposit to be processed on dYdX...')
wait_for_condition(
    lambda: len(client.private.get_transfers()['transfers']) > 0,
    True,
    60,
)
print('...transfer was recorded, waiting for confirmation...')
wait_for_condition(
    lambda: client.private.get_account()['account']['quoteBalance'],
    '2',
    180,
)
print('...done.')

# Post an order.
one_minute_from_now_iso = epoch_seconds_to_iso(time.time() + 60)
create_order_result = client.private.create_order(
    position_id=account['positionId'],
    market=constants.MARKET_BTC_USD,
    side=constants.ORDER_SIDE_BUY,
    order_type=constants.ORDER_TYPE_LIMIT,
    post_only=False,
    size='10',
    price='1000',
    limit_fee='0.1',
    expiration=one_minute_from_now_iso,
)

# Get the order.
order_id = create_order_result['order']['id']
print('order_id: ', order_id)
get_order_result = client.private.get_order_by_id(order_id)
assert get_order_result['order']['market'] == constants.MARKET_BTC_USD

# Cancel the order.
print('cancelling order_id, ', order_id)
client.private.cancel_order(order_id)

# Cancel all orders.
print('cancelling all orders')
client.private.cancel_all_orders()

# Get open orders.
get_orders_result = client.private.get_orders(
    market=constants.MARKET_BTC_USD,
    status=constants.POSITION_STATUS_OPEN,
)
assert get_orders_result == {'orders': []}

# Get fills.
get_fills_result = client.private.get_fills(
    market=constants.MARKET_BTC_USD,
)
print('fills object: ', get_fills_result)
