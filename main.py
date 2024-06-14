from bot.presale import monitor_wallet
import asyncio

if __name__ == '__main__':
    # Start monitoring the wallet
    asyncio.run(monitor_wallet())