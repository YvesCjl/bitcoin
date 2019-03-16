import hashlib
import json
import time
from eth_account import Account
from eth_account.messages import defunct_hash_message
from web3 import Web3, HTTPProvider, TestRPCProvider
from functools import reduce
import os

w3 = Web3( HTTPProvider( "http://127.0.0.1:8545" ) )
w3.eth.defaultAccount = w3.eth.accounts[-1]
contract = w3.eth.contract( address=open( "../contract/contract_address", "r" ).read().strip( '\n' ), abi=json.load( open( "../contract/contracts/contract.abi", "r" ) ) )

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
    #contract.functions.Test().call()

    resfil = contract.events.reg_done.createFilter( fromBlock=0 )
    contract.functions.register( account.address, name ).transact( transaction={ "gas":1145141919 } )
    for _ in range( 8 ):
        time.sleep( 2 )
        if reduce( lambda S, x: S or x.args[ "addr" ]==account.address and x.args[ "domainName" ]==name, resfil.get_new_entries(), False ):
            return True
    return False
    
    #txn = contract.functions.Test().transact( transaction={ "gas": 1145141919 } )
    #print( w3.eth.getTransactionReceipt( txn ) )
    #print( account.address )
    #print( w3.eth.account.recoverHash( defunct_hash_message( text=chal ), signature=vcode.signature ) )
	
print( register( "www.baidu.com" ) )
