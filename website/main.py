import hashlib
import json
from eth_account import Account
from eth_account.messages import defunct_hash_message
from web3 import Web3, HTTPProvider, TestRPCProvider
import os

w3 = Web3( HTTPProvider( "http://127.0.0.1:8545" ) )
w3.eth.defaultAccount = w3.eth.accounts[-1]
contract = w3.eth.contract( address="0xa2a5a412BB5D333D1F98D5e330059082a9f51866", abi=json.load( open( "../contract/contracts/contract.abi", "r" ) ) )

try:
    prkey = Account.decrypt( json.load( open( "./.keystore/key", "r" ) ), "123" )
except:
    prkey = Account.create().privateKey
    json.dump( Account.encrypt( prkey, "123" ), open( "./.keystore/key", "w" ) )
    w3.eth.sendTransaction( transaction={ "from": w3.eth.accounts[-1], "to": Account.privateKeyToAccount( prkey ).address, "value": int( 1e7 ) } )

account = Account.privateKeyToAccount( prkey )

def register( name ):
    fhash = hashlib.sha256( ( account.address+name ).encode( "utf8" ) ).hexdigest()
    path, chal = fhash[ :32 ], fhash[ 32: ]
    vcode = w3.eth.account.signHash( defunct_hash_message( text=chal ), private_key=prkey )
    with open( "./"+path, "wb" ) as fd:
        fd.write( vcode.signature )
    contract.functions.Test().call()
    contract.functions.register( account.address, name ).transact( transaction={ "gas":1145141919 } )
    print( account.address )
    print( w3.eth.account.recoverHash( defunct_hash_message( text=chal ), signature=vcode.signature ) )
	
register( "www.baidu.com" )
