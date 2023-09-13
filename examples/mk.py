from dydx3 import Client
from dydx3.constants import API_HOST_GOERLI
from dydx3.constants import NETWORK_ID_GOERLI
from web3 import Web3

WPU = "http://localhost:7545"

class MK(object):
	def __init__(self, address=None, pk=None, provider=WPU):
		self.address = address
		self.pk = pk
		self.provider = provider
		self.w3 = Web3(Web3.HTTPProvider(provider))
		self.client = self.build_client()
		self.stark = self.build_stark()
		self.onboard()
		self.query()

	def query(self):
		print('accounts_response')
		print(client.private.get_accounts())

	def onboard(self):
		print("onboard")
		onboarding_response = client.onboarding.create_user(
			stark_public_key=public_x,
			stark_public_key_y_coordinate=public_y
		)
		print('onboarding_response', onboarding_response)

	def build_stark(self):
		print("build stark")
		key_pair_with_y = self.client.onboarding.derive_stark_key()
		self.client.stark_private_key = key_pair_with_y['private_key']
		(self.public_x, self.public_y) = (
		    key_pair_with_y['public_key'],
		    key_pair_with_y['public_key_y_coordinate'],
		)

	def build_client(self):
		print("build client")
		clargs = {
			"host": API_HOST_GOERLI,
			"network_id": NETWORK_ID_GOERLI
		}
		if self.pk:
			clargs["eth_private_key"] = self.pk
		else:
			clargs["default_ethereum_address"] = self.address
		print("creating client with clargs:", clargs)
		return Client(**clargs)

if __name__ == "__main__":
	MK(input("ethereum address? "), input("private key? "),
		input("web provider? [default: %s]"%(WPU,)) or WPU)