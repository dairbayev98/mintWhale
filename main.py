import asyncio

import config
from client import Client
from tasks.whale_nft import WhaleNft

async def mint_for_all_keys():
    for private_key in config.PRIVATE_KEYS:
        try:
            print(f'Работаем с ключом: {private_key}')
            client = Client(
                private_key=private_key,
                rpc='https://polygon.llamarpc.com',
                proxy=config.PROXY
            )
            whale_nft = WhaleNft(client)
            mint_result = whale_nft.mint()
            print(f'Минт с ключом {private_key[:6]}... прошел успешно {mint_result}')
        except Exception as e:
            print(f'Ошибка с ключом {private_key[:6]}... {e}')
            print('test')



async def main():
    await mint_for_all_keys()

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())