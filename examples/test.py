import time

from web3 import Web3

from dydx3 import Client
from dydx3 import constants
from dydx3 import DydxApiError
from dydx3 import epoch_seconds_to_iso
from dydx3 import generate_private_key_hex_unsafe

SEVEN_DAYS_S = 7 * 24 * 60 * 60

web3_account = Web3(None).eth.account.create()
ethereum_address = web3_account.address
stark_private_key = generate_private_key_hex_unsafe()

print("ethereum_address: ", ethereum_address)
print("stark_private_key: ", stark_private_key)

# Create client for the new user.
client = Client(
    host="https://api.stage.dydx.exchange",
    network_id=5,
    stark_private_key=stark_private_key,
    web3_account=web3_account,
)

# Onboard the user.
client.onboarding.create_user()

# Register a new API key.
client.eth_private.create_api_key()

# Get the primary account.
get_account_result = client.private.get_account(
    ethereum_address=ethereum_address,
)
account = get_account_result.data['account']
assert int(account['starkKey'], 16) == int(client.stark_public_key, 16)

# Initiate a regular (slow) withdrawal.
#
# Expect signature validation to pass, although the collateralization
# check will fail.
expected_error = (
    'Withdrawal would put account under collateralization minumum'
)
expiration_epoch_seconds = time.time() + SEVEN_DAYS_S + 60
try:
    client.private.create_withdrawal(
        position_id=account['positionId'],
        amount='1',
        asset=constants.ASSET_USDC,
        to_address=ethereum_address,
        expiration_epoch_seconds=expiration_epoch_seconds,
    )
except DydxApiError as e:
    if expected_error not in str(e):
        raise

# Post an order.
#
# Expect signature validation to pass, although the collateralization
# check will fail.
one_minute_from_now_iso = epoch_seconds_to_iso(time.time() + 61)
try:
    client.private.create_order(
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
except DydxApiError as e:
    if expected_error not in str(e):
        raise
