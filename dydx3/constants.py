# ------------ API URLs ------------
API_HOST_MAINNET = 'https://api.dydx.exchange'
API_HOST_GOERLI = 'https://api.stage.dydx.exchange'
WS_HOST_MAINNET = 'wss://api.dydx.exchange/v3/ws'
WS_HOST_GOERLI = 'wss://api.stage.dydx.exchange/v3/ws'

# ------------ Ethereum Network IDs ------------
NETWORK_ID_MAINNET = 1
NETWORK_ID_GOERLI = 5

# ------------ Signature Types ------------
SIGNATURE_TYPE_NO_PREPEND = 0
SIGNATURE_TYPE_DECIMAL = 1
SIGNATURE_TYPE_HEXADECIMAL = 2

# ------------ Market Statistic Day Types ------------
MARKET_STATISTIC_DAY_ONE = '1'
MARKET_STATISTIC_DAY_SEVEN = '7'
MARKET_STATISTIC_DAY_THIRTY = '30'

# ------------ Order Types ------------
ORDER_TYPE_LIMIT = 'LIMIT'
ORDER_TYPE_MARKET = 'MARKET'
ORDER_TYPE_STOP = 'STOP_LIMIT'
ORDER_TYPE_TRAILING_STOP = 'TRAILING_STOP'
ORDER_TYPE_TAKE_PROFIT = 'TAKE_PROFIT'

# ------------ Order Side ------------
ORDER_SIDE_BUY = 'BUY'
ORDER_SIDE_SELL = 'SELL'

# ------------ Time in Force Types ------------
TIME_IN_FORCE_GTT = 'GTT'
TIME_IN_FORCE_FOK = 'FOK'
TIME_IN_FORCE_IOC = 'IOC'

# ------------ Position Status Types ------------
POSITION_STATUS_OPEN = 'OPEN'
POSITION_STATUS_CLOSED = 'CLOSED'
POSITION_STATUS_LIQUIDATED = 'LIQUIDATED'

# ------------ Order Status Types ------------
ORDER_STATUS_PENDING = 'PENDING'
ORDER_STATUS_OPEN = 'OPEN'
ORDER_STATUS_FILLED = 'FILLED'
ORDER_STATUS_CANCELED = 'CANCELED'
ORDER_STATUS_UNTRIGGERED = 'UNTRIGGERED'

# ------------ Transfer Status Types ------------
TRANSFER_STATUS_PENDING = 'PENDING'
TRANSFER_STATUS_CONFIRMED = 'CONFIRMED'
TRANSFER_STATUS_QUEUED = 'QUEUED'
TRANSFER_STATUS_CANCELED = 'CANCELED'
TRANSFER_STATUS_UNCONFIRMED = 'UNCONFIRMED'

# ------------ Account Action Types ------------
ACCOUNT_ACTION_DEPOSIT = 'DEPOSIT'
ACCOUNT_ACTION_WITHDRAWAL = 'WITHDRAWAL'

# ------------ Markets ------------
MARKET_BTC_USD = 'BTC-USD'
MARKET_ETH_USD = 'ETH-USD'
MARKET_LINK_USD = 'LINK-USD'
MARKET_AAVE_USD = 'AAVE-USD'
MARKET_UNI_USD = 'UNI-USD'
MARKET_SUSHI_USD = 'SUSHI-USD'
MARKET_SOL_USD = 'SOL-USD'
MARKET_YFI_USD = 'YFI-USD'
MARKET_ONEINCH_USD = '1INCH-USD'
MARKET_AVAX_USD = 'AVAX-USD'
MARKET_SNX_USD = 'SNX-USD'
MARKET_CRV_USD = 'CRV-USD'
MARKET_UMA_USD = 'UMA-USD'
MARKET_DOT_USD = 'DOT-USD'
MARKET_DOGE_USD = 'DOGE-USD'
MARKET_MATIC_USD = 'MATIC-USD'
MARKET_MKR_USD = 'MKR-USD'
MARKET_FIL_USD = 'FIL-USD'
MARKET_ADA_USD = 'ADA-USD'
MARKET_ATOM_USD = 'ATOM-USD'
MARKET_COMP_USD = 'COMP-USD'
MARKET_BCH_USD = 'BCH-USD'
MARKET_LTC_USD = 'LTC-USD'
MARKET_EOS_USD = 'EOS-USD'
MARKET_ALGO_USD = 'ALGO-USD'
MARKET_ZRX_USD = 'ZRX-USD'
MARKET_XMR_USD = 'XMR-USD'
MARKET_ZEC_USD = 'ZEC-USD'
MARKET_ENJ_USD = 'ENJ-USD'
MARKET_ETC_USD = 'ETC-USD'
MARKET_XLM_USD = 'XLM-USD'
MARKET_TRX_USD = 'TRX-USD'
MARKET_XTZ_USD = 'XTZ-USD'
MARKET_ICP_USD = 'ICP-USD'
MARKET_RUNE_USD = 'RUNE-USD'
MARKET_LUNA_USD = 'LUNA-USD'
MARKET_NEAR_USD = 'NEAR-USD'
MARKET_CELO_USD = 'CELO-USD'


# ------------ Assets ------------
ASSET_USDC = 'USDC'
ASSET_BTC = 'BTC'
ASSET_ETH = 'ETH'
ASSET_LINK = 'LINK'
ASSET_AAVE = 'AAVE'
ASSET_UNI = 'UNI'
ASSET_SUSHI = 'SUSHI'
ASSET_SOL = 'SOL'
ASSET_YFI = 'YFI'
ASSET_ONEINCH = '1INCH'
ASSET_AVAX = 'AVAX'
ASSET_SNX = 'SNX'
ASSET_CRV = 'CRV'
ASSET_UMA = 'UMA'
ASSET_DOT = 'DOT'
ASSET_DOGE = 'DOGE'
ASSET_MATIC = 'MATIC'
ASSET_MKR = 'MKR'
ASSET_FIL = 'FIL'
ASSET_ADA = 'ADA'
ASSET_ATOM = 'ATOM'
ASSET_COMP = 'COMP'
ASSET_BCH = 'BCH'
ASSET_LTC = 'LTC'
ASSET_EOS = 'EOS'
ASSET_ALGO = 'ALGO'
ASSET_ZRX = 'ZRX'
ASSET_XMR = 'XMR'
ASSET_ZEC = 'ZEC'
ASSET_ENJ = 'ENJ'
ASSET_ETC = 'ETC'
ASSET_XLM = 'XLM'
ASSET_TRX = 'TRX'
ASSET_XTZ = 'XTZ'
ASSET_ICP = 'ICP'
ASSET_RUNE = 'RUNE'
ASSET_LUNA = 'LUNA'
ASSET_NEAR = 'NEAR'
ASSET_CELO = 'CELO'
COLLATERAL_ASSET = ASSET_USDC

# ------------ Synthetic Assets by Market ------------
SYNTHETIC_ASSET_MAP = {
    MARKET_BTC_USD: ASSET_BTC,
    MARKET_ETH_USD: ASSET_ETH,
    MARKET_LINK_USD: ASSET_LINK,
    MARKET_AAVE_USD: ASSET_AAVE,
    MARKET_UNI_USD: ASSET_UNI,
    MARKET_SUSHI_USD: ASSET_SUSHI,
    MARKET_SOL_USD: ASSET_SOL,
    MARKET_YFI_USD: ASSET_YFI,
    MARKET_ONEINCH_USD: ASSET_ONEINCH,
    MARKET_AVAX_USD: ASSET_AVAX,
    MARKET_SNX_USD: ASSET_SNX,
    MARKET_CRV_USD: ASSET_CRV,
    MARKET_UMA_USD: ASSET_UMA,
    MARKET_DOT_USD: ASSET_DOT,
    MARKET_DOGE_USD: ASSET_DOGE,
    MARKET_MATIC_USD: ASSET_MATIC,
    MARKET_MKR_USD: ASSET_MKR,
    MARKET_FIL_USD: ASSET_FIL,
    MARKET_ADA_USD: ASSET_ADA,
    MARKET_ATOM_USD: ASSET_ATOM,
    MARKET_COMP_USD: ASSET_COMP,
    MARKET_BCH_USD: ASSET_BCH,
    MARKET_LTC_USD: ASSET_LTC,
    MARKET_EOS_USD: ASSET_EOS,
    MARKET_ALGO_USD: ASSET_ALGO,
    MARKET_ZRX_USD: ASSET_ZRX,
    MARKET_XMR_USD: ASSET_XMR,
    MARKET_ZEC_USD: ASSET_ZEC,
    MARKET_ENJ_USD: ASSET_ENJ,
    MARKET_ETC_USD: ASSET_ETC,
    MARKET_XLM_USD: ASSET_XLM,
    MARKET_TRX_USD: ASSET_TRX,
    MARKET_XTZ_USD: ASSET_XTZ,
    MARKET_ICP_USD: ASSET_ICP,
    MARKET_RUNE_USD: ASSET_RUNE,
    MARKET_LUNA_USD: ASSET_LUNA,
    MARKET_NEAR_USD: ASSET_NEAR,
    MARKET_CELO_USD: ASSET_CELO,
}

# ------------ Asset IDs ------------
COLLATERAL_ASSET_ID_BY_NETWORK_ID = {
    NETWORK_ID_MAINNET: int(
        '0x02893294412a4c8f915f75892b395ebbf6859ec246ec365c3b1f56f47c3a0a5d',
        16,
    ),
    NETWORK_ID_GOERLI: int(
        '0x03bda2b4764039f2df44a00a9cf1d1569a83f95406a983ce4beb95791c376008',
        16,
    ),
}
SYNTHETIC_ASSET_ID_MAP = {
    ASSET_BTC: int('0x4254432d3130000000000000000000', 16),
    ASSET_ETH: int('0x4554482d3900000000000000000000', 16),
    ASSET_LINK: int('0x4c494e4b2d37000000000000000000', 16),
    ASSET_AAVE: int('0x414156452d38000000000000000000', 16),
    ASSET_UNI: int('0x554e492d3700000000000000000000', 16),
    ASSET_SUSHI: int('0x53555348492d370000000000000000', 16),
    ASSET_SOL: int('0x534f4c2d3700000000000000000000', 16),
    ASSET_YFI: int('0x5946492d3130000000000000000000', 16),
    ASSET_ONEINCH: int('0x31494e43482d370000000000000000', 16),
    ASSET_AVAX: int('0x415641582d37000000000000000000', 16),
    ASSET_SNX: int('0x534e582d3700000000000000000000', 16),
    ASSET_CRV: int('0x4352562d3600000000000000000000', 16),
    ASSET_UMA: int('0x554d412d3700000000000000000000', 16),
    ASSET_DOT: int('0x444f542d3700000000000000000000', 16),
    ASSET_DOGE: int('0x444f47452d35000000000000000000', 16),
    ASSET_MATIC: int('0x4d415449432d360000000000000000', 16),
    ASSET_MKR: int('0x4d4b522d3900000000000000000000', 16),
    ASSET_FIL: int('0x46494c2d3700000000000000000000', 16),
    ASSET_ADA: int('0x4144412d3600000000000000000000', 16),
    ASSET_ATOM: int('0x41544f4d2d37000000000000000000', 16),
    ASSET_COMP: int('0x434f4d502d38000000000000000000', 16),
    ASSET_BCH: int('0x4243482d3800000000000000000000', 16),
    ASSET_LTC: int('0x4c54432d3800000000000000000000', 16),
    ASSET_EOS: int('0x454f532d3600000000000000000000', 16),
    ASSET_ALGO: int('0x414c474f2d36000000000000000000', 16),
    ASSET_ZRX: int('0x5a52582d3600000000000000000000', 16),
    ASSET_XMR: int('0x584d522d3800000000000000000000', 16),
    ASSET_ZEC: int('0x5a45432d3800000000000000000000', 16),
    ASSET_ENJ: int('0x454e4a2d3600000000000000000000', 16),
    ASSET_ETC: int('0x4554432d3700000000000000000000', 16),
    ASSET_XLM: int('0x584c4d2d3500000000000000000000', 16),
    ASSET_TRX: int('0x5452582d3400000000000000000000', 16),
    ASSET_XTZ: int('0x58545a2d3600000000000000000000', 16),
    ASSET_ICP: int('0x4943502d3700000000000000000000', 16),
    ASSET_RUNE: int('0x52554e452d36000000000000000000', 16),
    ASSET_LUNA: int('0x4c554e412d36000000000000000000', 16),
    ASSET_NEAR: int('0x4e4541522d36000000000000000000', 16),
    ASSET_CELO: int('0x43454c4f2d36000000000000000000', 16),
}


# ------------ Asset Resolution (Quantum Size) ------------
#
# The asset resolution is the number of quantums (Starkware units) that fit
# within one "human-readable" unit of the asset. For example, if the asset
# resolution for BTC is 1e10, then the smallest unit representable within
# Starkware is 1e-10 BTC, i.e. 1/100th of a satoshi.
#
# For the collateral asset (USDC), the chosen resolution corresponds to the
# base units of the ERC-20 token. For the other, synthetic, assets, the
# resolutions are chosen such that prices relative to USDC are close to one.
ASSET_RESOLUTION = {
    ASSET_USDC: '1e6',
    ASSET_BTC: '1e10',
    ASSET_ETH: '1e9',
    ASSET_LINK: '1e7',
    ASSET_AAVE: '1e8',
    ASSET_UNI: '1e7',
    ASSET_SUSHI: '1e7',
    ASSET_SOL: '1e7',
    ASSET_YFI: '1e10',
    ASSET_ONEINCH: '1e7',
    ASSET_AVAX: '1e7',
    ASSET_SNX: '1e7',
    ASSET_CRV: '1e6',
    ASSET_UMA: '1e7',
    ASSET_DOT: '1e7',
    ASSET_DOGE: '1e5',
    ASSET_MATIC: '1e6',
    ASSET_MKR: '1e9',
    ASSET_FIL: '1e7',
    ASSET_ADA: '1e6',
    ASSET_ATOM: '1e7',
    ASSET_COMP: '1e8',
    ASSET_BCH: '1e8',
    ASSET_LTC: '1e8',
    ASSET_EOS: '1e6',
    ASSET_ALGO: '1e6',
    ASSET_ZRX: '1e6',
    ASSET_XMR: '1e8',
    ASSET_ZEC: '1e8',
    ASSET_ENJ: '1e6',
    ASSET_ETC: '1e7',
    ASSET_XLM: '1e5',
    ASSET_TRX: '1e4',
    ASSET_XTZ: '1e6',
    ASSET_ICP: '1e7',
    ASSET_RUNE: '1e6',
    ASSET_LUNA: '1e6',
    ASSET_NEAR: '1e6',
    ASSET_CELO: '1e6',
}

# ------------ Ethereum Transactions ------------
DEFAULT_GAS_AMOUNT = hex(250000)
DEFAULT_GAS_MULTIPLIER = 1.5
DEFAULT_GAS_PRICE = 4000000000
DEFAULT_GAS_PRICE_ADDITION = 3
MAX_SOLIDITY_UINT = 115792089237316195423570985008687907853269984665640564039457584007913129639935  # noqa: E501
FACT_REGISTRY_CONTRACT = {
    NETWORK_ID_MAINNET: '0xBE9a129909EbCb954bC065536D2bfAfBd170d27A',
    NETWORK_ID_GOERLI: '0xc5061C08cF892C79DDB106B777138982433C8865',
}
STARKWARE_PERPETUALS_CONTRACT = {
    NETWORK_ID_MAINNET: '0xD54f502e184B6B739d7D27a6410a67dc462D69c8',
    NETWORK_ID_GOERLI: '0xFE76edf35648Cc733d57200646cb1Dc63d05462F',
}
TOKEN_CONTRACTS = {
    ASSET_USDC: {
        NETWORK_ID_MAINNET: '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
        NETWORK_ID_GOERLI: '0xF7a2fa2c2025fFe64427dd40Dc190d47ecC8B36e',
    },
}
COLLATERAL_TOKEN_DECIMALS = 6

# ------------ Off-Chain Ethereum-Signed Actions ------------
OFF_CHAIN_ONBOARDING_ACTION = 'dYdX Onboarding'
OFF_CHAIN_KEY_DERIVATION_ACTION = 'dYdX STARK Key'


# ------------ API Defaults ------------
DEFAULT_API_TIMEOUT = 3000
