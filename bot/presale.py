from web3 import Web3
from telegram import Bot
import time
import json
from pprint import pprint
from datetime import datetime
from telegram import Bot
import asyncio
import os 

file_path = os.path.dirname(__file__)

img_path = os.path.join(file_path, "presale.png")
TOKEN = "7311342048:AAFvXN29Dabf9wX0BSxOh3kMfdv_M1mzm6U"
bot = Bot(token=TOKEN)
CHAT_ID = -1002158724916
# Load configurations from a config file or environment variables
rpc_url = "https://ethereum-rpc.publicnode.com"
ETH_WALLET = '0x55B4A5cA9C919D74713Dc6c46CC37140cc626Ee9'
TELEGRAM_API_TOKEN = '7311342048:AAFvXN29Dabf9wX0BSxOh3kMfdv_M1mzm6U'
# TELEGRAM_CHAT_ID = 'YOUR_TELEGRAM_CHAT_ID'
abi =[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":True,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"Customer","outputs":[{"internalType":"uint256","name":"tokensBought","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"buyTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"buyTokensWithUSDT","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_usdtRate","type":"uint256"},{"internalType":"uint256","name":"_ethToUsd","type":"uint256"},{"internalType":"uint256","name":"divider","type":"uint256"},{"internalType":"uint256","name":"usdtDiv","type":"uint256"}],"name":"changeRate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address payable","name":"_wallet","type":"address"}],"name":"changeWallet","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"checkPresaleEnd","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"checkPresaleStatus","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"checkbalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claimTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"deposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"endPresale","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"ethDivider","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getClaimableTokens","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getDivider","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getETHPriceInUSD","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTokenUsdPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getUsdtDivider","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getUsdtRate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"priceOracle","outputs":[{"internalType":"contract ChainlinkPriceOracle","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"progressETH","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"progressUSDT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"soldTokens","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"startPresale","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"token","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"tokenPriceUSD","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"usdt","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"wallet","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]
web3 = Web3(Web3.HTTPProvider(rpc_url))
contract = web3.eth.contract(address=ETH_WALLET, abi=abi)

def get_amount_in_usd(amount_in_ether):
    try:
        usd = contract.functions.getETHPriceInUSD().call()
        usd_amount = format(usd * amount_in_ether, '.4f')
        return usd_amount
    except Exception as e:
        print(f"Error fetching USD price: {e}")
        return None


def get_time_and_status(hash):
    txn_receipt = web3.eth.get_transaction_receipt(hash)
    block = web3.eth.get_block(txn_receipt.blockNumber)
    txn_timestamp = datetime.fromtimestamp(block.timestamp)
    timestamp = datetime.strptime(str(txn_timestamp), "%Y-%m-%d %H:%M:%S")
    timestamp = timestamp.strftime("%B-%d-%Y %H:%M:%S")
    txn_status = txn_receipt.status
    if txn_status:
        status = "success"
    else:
        status = "failure"
    print(status)
    return timestamp, status

async def send_telegram_message(message):
    await bot.send_photo(photo=img_path,chat_id=CHAT_ID, caption=message,parse_mode="HTML")
    

async def monitor_wallet():
    transaction_details = {}
    
    # Load the last processed block number and transactions from a file or initialize them
    try:
        with open('last_block.txt', 'r') as f:
            last_block = int(f.read().strip())
        with open('processed_txs.txt', 'r') as f:
            processed_txs = set(f.read().splitlines())
    except FileNotFoundError:
        last_block = web3.eth.block_number
        processed_txs = set()
    
    while True:
        
        latest_block = web3.eth.block_number
        if latest_block > last_block:
            latest_block = 20091906
            print(f'Processing block {latest_block}...')
            block = web3.eth.get_block(latest_block, full_transactions=True)
            
            for tx in block.transactions:
                tx_hash = tx['hash'].hex()
                if tx.to and str(tx.to).lower() == ETH_WALLET.lower():
                    if tx_hash not in processed_txs:
                        transaction_details['tnxHash'] = tx_hash
                        transaction_details['from'] = tx['from']
                        transaction_details['to'] = tx['to']
                        transaction_details['value'] = web3.from_wei(tx['value'], 'ether')
                        transaction_details['gasPrice'] = web3.from_wei(tx['gasPrice'], 'gwei')
                        transaction_details['blockNumber'] = tx['blockNumber']
                        transaction_details['transactionIndex'] = tx['transactionIndex']
                        transaction_details['method'] = 'Buy Tokens'
                        transaction_details['methodID'] = web3.keccak(text="buyTokens()").hex()[:10]
                        timespan, status = get_time_and_status(tx_hash)
                        transaction_details['Timespan'] = timespan
                        transaction_details['status'] = status
                        amount_usd = get_amount_in_usd(transaction_details['value'])
                        print(amount_usd)
                        pprint(transaction_details)
                        message = f"""
  🚨 Alert 🚨   
                     
🤖<b>New Transaction Detected</b>🤖
#️⃣<b>Hash:</b> <code>{transaction_details['tnxHash']}</code>
💰<b>Amount:</b> <u>{transaction_details['value']} ETH</u>
💰<b>Amount(USD):</b> <u>${amount_usd}</u>
👩‍💻<b>Block Number:</b> {transaction_details['blockNumber']}
🌐<b>Transaction Index:</b> {transaction_details['transactionIndex']}
🔗<b>Method:</b> {transaction_details['method']}
⌚<b>Timestamp:</b> {transaction_details['Timespan']}
🚀<b>Status:</b> {transaction_details['status']}

<a href="https://etherscan.io/tx/{tx_hash}">🔥View Transaction 🔥</a>
"""
                        await send_telegram_message(message)
                        
                        processed_txs.add(tx_hash)
            
            # Update the last processed block number
            last_block = latest_block
            with open('last_block.txt', 'w') as f:
                f.write(str(last_block))
            with open('processed_txs.txt', 'w') as f:
                f.write('\n'.join(processed_txs))
        
        time.sleep(10)

# Start monitoring the wallet
asyncio.run(monitor_wallet())

