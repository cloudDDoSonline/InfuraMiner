from hashlib import sha256
from web3 import Web3
import os
import time

os.system ( "InfuraMiner" )
web3 = Web3 ( Web3.HTTPProvider ( "https://mainnet.infura.io/v3/1ee116a4d01f45848f4df84bd2ffd23c" ) )
print ( "Подключен к Web3: " , web3.isConnected () )
to_account = str ( input ( "Импортируйте свой кошелек: " ) )
balance = web3.eth.get_balance ( to_account )
print ( "Ваш текущий баланс" , balance , "ETH." )
time.sleep ( 1 )
difficulty = int ( input ( "Выберите сложность (рекомендуется 13 или выше): " ) )
MAX_NONCE = 100000000000


def SHA256(text):
    return sha256 ( text.encode ( "ascii" ) ).hexdigest ()


def mine(block_number , transactions , previous_hash , prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range ( MAX_NONCE ):
        text = str ( block_number ) + transactions + previous_hash + str ( nonce )
        new_hash = SHA256 ( text )
        if new_hash.startswith ( prefix_str ):
            print ( f"ура! Успешно добыт ETH с одноразовым номером value:{nonce}" )
            return new_hash

    raise BaseException ( f"Не удалось найти правильный хэш после попытки {MAX_NONCE} times" )


if __name__ == '__main__':
    transactions = '''
    Dhaval->Bhavin->20,
    Mando->Cara->45
    '''
    start = time.time ()
    print ( "Начал майнинг..." )
    new_hash = mine ( 5 , transactions , '0x0fc2008d1fc2ba5a41b61497f802b830a50c2ae2ba05cf9611545b72ebe1204f' , difficulty )
    total_time = str ( (time.time () - start) )
    print ( f"Закончил майнинг! Добыча заняла: {total_time} seconds." )
    print ( "Хэш добывается: " , new_hash )
