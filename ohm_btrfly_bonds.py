import os
import json
import decimal
from web3 import Web3
import discord
from discord.ext import commands, tasks
from pycoingecko import CoinGeckoAPI

BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN_REDACTED_OHM_LP"]

# Initialize Discord client
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(intents=intents, help_command=None)

# Initialize web3
INFURA_TOKEN = os.environ['WEB3_INFURA_TOKEN_4']
infuraURL = f'https://mainnet.infura.io/v3/{INFURA_TOKEN}'
web3 = Web3(Web3.HTTPProvider(infuraURL))


def bond_calculator(bond_calc_address):
    bond_calc_abi = json.loads('[{"inputs":[{"internalType":"address","name":"_BTRFLY","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"BTRFLY","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"valuation","outputs":[{"internalType":"uint256","name":"value_","type":"uint256"}],"stateMutability":"view","type":"function"}]')
    bondCalculator = web3.eth.contract(address=bond_calc_address, abi=bond_calc_abi)
    depositValue = bondCalculator.functions.valuation('0xe9AB8038Ee6Dd4fCC7612997FE28d4e22019C4B4', 1000000000).call()

    return depositValue


def deposit_in_btrfly(lp_address):
    lp_abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"sync","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]')
    lpToken = web3.eth.contract(address=lp_address, abi=lp_abi)
    
    btrfly_address = '0xC0d4Ceb216B3BA9C3701B291766fDCbA977ceC3A'
    btrfly_abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account_","type":"address"},{"internalType":"uint256","name":"amount_","type":"uint256"}],"name":"_burnFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"authorisedOperatorsArray","type":"address[]"}],"name":"addBatchAuthorisedOperators","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account_","type":"address"},{"internalType":"uint256","name":"amount_","type":"uint256"}],"name":"burnFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"status","type":"bool"}],"name":"changeAuthorisation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"isAuthorisedOperators","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isTokenFrozen","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account_","type":"address"},{"internalType":"uint256","name":"amount_","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"vault_","type":"address"}],"name":"setVault","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner_","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"unFreezeToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"vault","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]')
    btrfly = web3.eth.contract(address=btrfly_address, abi=btrfly_abi)

    try:
        lpSupply = lpToken.functions.totalSupply().call()
        lpBtrflyBalance = btrfly.functions.balanceOf(lp_address).call()
        lpDepositBtrflyValue = 2*lpBtrflyBalance*1E9/lpSupply

        return lpDepositBtrflyValue

    except Exception as e:
        print(e)


def bond_discount(bond_address, depositValue):
    abi = json.loads('[{"inputs":[{"internalType":"address","name":"_BTRFLY","type":"address"},{"internalType":"address","name":"_principal","type":"address"},{"internalType":"address","name":"_treasury","type":"address"},{"internalType":"address","name":"_DAO","type":"address"},{"internalType":"address","name":"_bondCalculator","type":"address"},{"internalType":"address","name":"_OLYMPUSDAO","type":"address"},{"internalType":"address","name":"_OLYMPUSTreasury","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"deposit","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"payout","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"expires","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"nativePrice","type":"uint256"}],"name":"BondCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"nativePrice","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"internalPrice","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"debtRatio","type":"uint256"}],"name":"BondPriceChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"payout","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"remaining","type":"uint256"}],"name":"BondRedeemed","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"initialBCV","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newBCV","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"adjustment","type":"uint256"},{"indexed":false,"internalType":"bool","name":"addition","type":"bool"}],"name":"ControlVariableAdjustment","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipPulled","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipPushed","type":"event"},{"inputs":[],"name":"BTRFLY","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DAO","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"OLYMPUSDAO","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"OLYMPUSTreasury","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"adjustment","outputs":[{"internalType":"bool","name":"add","type":"bool"},{"internalType":"uint256","name":"rate","type":"uint256"},{"internalType":"uint256","name":"target","type":"uint256"},{"internalType":"uint256","name":"buffer","type":"uint256"},{"internalType":"uint256","name":"lastBlock","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"bondCalculator","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"bondInfo","outputs":[{"internalType":"uint256","name":"payout","type":"uint256"},{"internalType":"uint256","name":"vesting","type":"uint256"},{"internalType":"uint256","name":"lastBlock","type":"uint256"},{"internalType":"uint256","name":"pricePaid","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"bondPrice","outputs":[{"internalType":"uint256","name":"price_","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"bondPriceInUSD","outputs":[{"internalType":"uint256","name":"price_","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"currentDebt","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"debtDecay","outputs":[{"internalType":"uint256","name":"decay_","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"debtRatio","outputs":[{"internalType":"uint256","name":"debtRatio_","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_maxPrice","type":"uint256"},{"internalType":"address","name":"_depositor","type":"address"}],"name":"deposit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_controlVariable","type":"uint256"},{"internalType":"uint256","name":"_vestingTerm","type":"uint256"},{"internalType":"uint256","name":"_minimumPrice","type":"uint256"},{"internalType":"uint256","name":"_maxPayout","type":"uint256"},{"internalType":"uint256","name":"_fee","type":"uint256"},{"internalType":"uint256","name":"_maxDebt","type":"uint256"},{"internalType":"uint256","name":"_tithe","type":"uint256"},{"internalType":"uint256","name":"_initialDebt","type":"uint256"}],"name":"initializeBondTerms","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"isLiquidityBond","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lastDecay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxPayout","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"payoutFor","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_depositor","type":"address"}],"name":"pendingPayoutFor","outputs":[{"internalType":"uint256","name":"pendingPayout_","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_depositor","type":"address"}],"name":"percentVestedFor","outputs":[{"internalType":"uint256","name":"percentVested_","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"policy","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"principal","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pullManagement","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner_","type":"address"}],"name":"pushManagement","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"}],"name":"recoverLostToken","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_recipient","type":"address"},{"internalType":"bool","name":"_stake","type":"bool"}],"name":"redeem","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceManagement","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_addition","type":"bool"},{"internalType":"uint256","name":"_increment","type":"uint256"},{"internalType":"uint256","name":"_target","type":"uint256"},{"internalType":"uint256","name":"_buffer","type":"uint256"}],"name":"setAdjustment","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"enum REDACTEDBondDepositoryRewardBased.PARAMETER","name":"_parameter","type":"uint8"},{"internalType":"uint256","name":"_input","type":"uint256"}],"name":"setBondTerms","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_newTreasury","type":"address"}],"name":"setOLYMPUSTreasury","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_staking","type":"address"},{"internalType":"bool","name":"_helper","type":"bool"}],"name":"setStaking","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"staking","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"stakingHelper","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"standardizedDebtRatio","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"terms","outputs":[{"internalType":"uint256","name":"controlVariable","type":"uint256"},{"internalType":"uint256","name":"vestingTerm","type":"uint256"},{"internalType":"uint256","name":"minimumPrice","type":"uint256"},{"internalType":"uint256","name":"maxPayout","type":"uint256"},{"internalType":"uint256","name":"fee","type":"uint256"},{"internalType":"uint256","name":"tithe","type":"uint256"},{"internalType":"uint256","name":"maxDebt","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalDebt","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"treasury","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"useHelper","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]')  # noqa: E501
    bond = web3.eth.contract(address=bond_address, abi=abi)
    
    try:
        payout = bond.functions.payoutFor(depositValue).call()
        return payout

    except Exception as e:
        print(e)


def maxDebtReached(bond_address):
    abi = json.loads('[{"inputs":[{"internalType":"address","name":"_BTRFLY","type":"address"},{"internalType":"address","name":"_principal","type":"address"},{"internalType":"address","name":"_treasury","type":"address"},{"internalType":"address","name":"_DAO","type":"address"},{"internalType":"address","name":"_bondCalculator","type":"address"},{"internalType":"address","name":"_OLYMPUSDAO","type":"address"},{"internalType":"address","name":"_OLYMPUSTreasury","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"deposit","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"payout","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"expires","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"nativePrice","type":"uint256"}],"name":"BondCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"nativePrice","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"internalPrice","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"debtRatio","type":"uint256"}],"name":"BondPriceChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"payout","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"remaining","type":"uint256"}],"name":"BondRedeemed","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"initialBCV","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newBCV","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"adjustment","type":"uint256"},{"indexed":false,"internalType":"bool","name":"addition","type":"bool"}],"name":"ControlVariableAdjustment","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipPulled","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipPushed","type":"event"},{"inputs":[],"name":"BTRFLY","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DAO","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"OLYMPUSDAO","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"OLYMPUSTreasury","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"adjustment","outputs":[{"internalType":"bool","name":"add","type":"bool"},{"internalType":"uint256","name":"rate","type":"uint256"},{"internalType":"uint256","name":"target","type":"uint256"},{"internalType":"uint256","name":"buffer","type":"uint256"},{"internalType":"uint256","name":"lastBlock","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"bondCalculator","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"bondInfo","outputs":[{"internalType":"uint256","name":"payout","type":"uint256"},{"internalType":"uint256","name":"vesting","type":"uint256"},{"internalType":"uint256","name":"lastBlock","type":"uint256"},{"internalType":"uint256","name":"pricePaid","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"bondPrice","outputs":[{"internalType":"uint256","name":"price_","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"bondPriceInUSD","outputs":[{"internalType":"uint256","name":"price_","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"currentDebt","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"debtDecay","outputs":[{"internalType":"uint256","name":"decay_","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"debtRatio","outputs":[{"internalType":"uint256","name":"debtRatio_","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_maxPrice","type":"uint256"},{"internalType":"address","name":"_depositor","type":"address"}],"name":"deposit","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_controlVariable","type":"uint256"},{"internalType":"uint256","name":"_vestingTerm","type":"uint256"},{"internalType":"uint256","name":"_minimumPrice","type":"uint256"},{"internalType":"uint256","name":"_maxPayout","type":"uint256"},{"internalType":"uint256","name":"_fee","type":"uint256"},{"internalType":"uint256","name":"_maxDebt","type":"uint256"},{"internalType":"uint256","name":"_tithe","type":"uint256"},{"internalType":"uint256","name":"_initialDebt","type":"uint256"}],"name":"initializeBondTerms","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"isLiquidityBond","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lastDecay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxPayout","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"payoutFor","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_depositor","type":"address"}],"name":"pendingPayoutFor","outputs":[{"internalType":"uint256","name":"pendingPayout_","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_depositor","type":"address"}],"name":"percentVestedFor","outputs":[{"internalType":"uint256","name":"percentVested_","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"policy","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"principal","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pullManagement","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner_","type":"address"}],"name":"pushManagement","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"}],"name":"recoverLostToken","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_recipient","type":"address"},{"internalType":"bool","name":"_stake","type":"bool"}],"name":"redeem","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceManagement","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_addition","type":"bool"},{"internalType":"uint256","name":"_increment","type":"uint256"},{"internalType":"uint256","name":"_target","type":"uint256"},{"internalType":"uint256","name":"_buffer","type":"uint256"}],"name":"setAdjustment","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"enum REDACTEDBondDepositoryRewardBased.PARAMETER","name":"_parameter","type":"uint8"},{"internalType":"uint256","name":"_input","type":"uint256"}],"name":"setBondTerms","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_newTreasury","type":"address"}],"name":"setOLYMPUSTreasury","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_staking","type":"address"},{"internalType":"bool","name":"_helper","type":"bool"}],"name":"setStaking","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"staking","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"stakingHelper","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"standardizedDebtRatio","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"terms","outputs":[{"internalType":"uint256","name":"controlVariable","type":"uint256"},{"internalType":"uint256","name":"vestingTerm","type":"uint256"},{"internalType":"uint256","name":"minimumPrice","type":"uint256"},{"internalType":"uint256","name":"maxPayout","type":"uint256"},{"internalType":"uint256","name":"fee","type":"uint256"},{"internalType":"uint256","name":"tithe","type":"uint256"},{"internalType":"uint256","name":"maxDebt","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalDebt","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"treasury","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"useHelper","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]')  # noqa: E501
    bond = web3.eth.contract(address=bond_address, abi=abi)
    try:
        currentDebt = bond.functions.currentDebt().call()
        maxDebt = bond.functions.terms().call()
        if currentDebt >= maxDebt[-1]:
            return True
        else:
            return False

    except Exception as e:
        print("maxDebtReached error")
        print(e)    


def get_discounts():
    #check if max debt is reached
    bondClosed = maxDebtReached(bond_address='0x1fDf1233f85A3BAe9594B0558e4EC8Febe8c6720')

    if bondClosed is True:
        return -999
    else:
        try:
            lpDeposit = deposit_in_btrfly(lp_address = '0xe9AB8038Ee6Dd4fCC7612997FE28d4e22019C4B4')
            depositValue = bond_calculator(bond_calc_address = '0xa77b57445FA262CaE325DeD434Df89302c93f59A')
            payout = bond_discount(bond_address='0x1fDf1233f85A3BAe9594B0558e4EC8Febe8c6720', depositValue=depositValue)
        
            return ((payout / lpDeposit) - 1)
            
        except Exception as e:
            print(e)


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    if not check_discounts.is_running():
        check_discounts.start()


@tasks.loop(seconds = 90)
async def check_discounts():
    bondDisc = get_discounts()
    
    for guild in client.guilds:
        guser = guild.get_member(client.user.id)
        try:
            if bondDisc == -999:
                await guser.edit(nick=f'Sold Out!')
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f'⛔ OHM-BTRFLY Bonds'))
            elif bondDisc < 0:
                await guser.edit(nick=f'{-100*bondDisc:,.2f}% Premium')
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f'OHM-BTRFLY Bonds'))
            else:
                await guser.edit(nick=f'{100*bondDisc:,.2f}% Discount')
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f'OHM-BTRFLY Bonds'))

        except Exception as e:
            print("check_discounts error")
            print(e)


client.run(BOT_TOKEN)