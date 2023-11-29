'''Example for placing, replacing, and canceling orders.

Usage: python -m examples.orders
'''

import time

from dydx3 import Client
from dydx3.constants import API_HOST_GOERLI
from dydx3.constants import MARKET_BTC_USD
from dydx3.constants import NETWORK_ID_GOERLI
from dydx3.constants import ORDER_SIDE_BUY
from dydx3.constants import ORDER_STATUS_OPEN
from dydx3.constants import ORDER_TYPE_LIMIT
from web3 import Web3

# Ganache test address.
ETHEREUM_ADDRESS = '0xF7e34Ace3531a2e82220BE81e0B6fEf0cD9Eb3cF'

# Ganache node.
WEB_PROVIDER_URL = 'http://localhost:8545'

stark_creds = {
    'public_key': (
        '0x4be43e3005985ffd8b2f2bcc8247d5889d3abfd07bf53635cf5f0b5ea10d598'
    ),
    'public_key_y_coordinate': (
        '0x434a44012e7bcfba8d7e1c4814bf17d367b5f1927ac1764a26509367dc6bb08'
    ),
    'private_key': (
        '0xb55fd6a7cb7e37b9448a49ca3119c90bcb7c4e6ac3d4a5dcd36b2692342b7f'
    )
}

print("CREATING CLIENT\n")
client = Client(
    network_id=NETWORK_ID_GOERLI,
    host=API_HOST_GOERLI,
    default_ethereum_address=ETHEREUM_ADDRESS,
    stark_private_key=stark_creds['private_key'],
    stark_public_key=stark_creds['public_key'],
    stark_public_key_y_coordinate=stark_creds['public_key_y_coordinate'],
    web3=Web3(Web3.HTTPProvider(WEB_PROVIDER_URL))
)

# Set STARK key.
# print("CREATING STARK PK\n")
# stark_private_key = client.onboarding.derive_stark_key()
# client.stark_private_key = stark_private_key['private_key']
# client.onboarding.stark_public_key = stark_private_key['public_key']
# client.onboarding.stark_public_key_y_coordinate = (
#     stark_private_key['public_key_y_coordinate']
# )
# print("stark_private_key: ", stark_private_key, "\n")

# print("ONBOARDING CREATING USER\n")
# client.onboarding.create_user()

# Get our position ID.
print("REQUESTING CLIENT PRIVATE ACCOUNT\n")
account_response = client.private.get_account()
print("account_response: ", account_response)
position_id = account_response.data['account']['positionId']
print("position_id: ", position_id, "\n")

# Post an bid at a price that is unlikely to match.
order_params = {
    'position_id': position_id,
    'market': MARKET_BTC_USD,
    'side': ORDER_SIDE_BUY,
    'order_type': ORDER_TYPE_LIMIT,
    'post_only': True,
    'size': '0.0777',
    'price': '20',
    'limit_fee': '0.0015',
    'expiration_epoch_seconds': time.time() + 65,
}
order_response = client.private.create_order(**order_params)
order_id = order_response.data['order']['id']

# Replace the order at a higher price, several times.
# Note that order replacement is done atomically in the matching engine.
for replace_price in range(21, 26):
    order_response = client.private.create_order(
        **dict(
            order_params,
            price=str(replace_price),
            cancel_id=order_id,
        ),
    )
    order_id = order_response.data['order']['id']

# Count open orders (there should be exactly one).
orders_response = client.private.get_orders(
    market=MARKET_BTC_USD,
    status=ORDER_STATUS_OPEN,
)
print("orders data: ", orders_response.data, "\n")
assert len(orders_response.data['orders']) == 1
#
# Cancel all orders.
# client.private.cancel_all_orders()
#
# # Count open orders (there should be none).
# orders_response = client.private.get_orders(
#     market=MARKET_BTC_USD,
#     status=ORDER_STATUS_OPEN,
# )
# assert len(orders_response.data['orders']) == 0
