from tracker.erc20_abi import ERC20_ABI
from tracker.models import Token
from web3.main import Web3


def check_supply_for(token: Token) -> float:
    w3 = Web3(Web3.HTTPProvider(token.network.rpc_url))
    contract = w3.eth.contract(
        address=Web3.toChecksumAddress(token.contract_address), abi=ERC20_ABI
    )

    return contract.functions.totalSupply().call()
