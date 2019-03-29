import hashlib
import json
import time
from eth_account import Account
from eth_account.messages import defunct_hash_message
from web3 import Web3, HTTPProvider, TestRPCProvider
from functools import reduce
import os

w3 = Web3( HTTPProvider( "http://127.0.0.1:8545" ) )
conaddr = open( "../contract/contract_address", "r" ).read().strip( '\n' )
contract = w3.eth.contract( address=conaddr, abi=json.load( open( "../contract/contracts/contract.abi", "r" ) ) )

try:
    prkey = Account.decrypt( json.load( open( "./.keystore/key", "r" ) ), "123" )
except:
    prkey = Account.create().privateKey
    json.dump( Account.encrypt( prkey, "123" ), open( "./.keystore/key", "w" ) )
w3.eth.sendTransaction( transaction={ "from": w3.eth.accounts[-1], "to": Account.privateKeyToAccount( prkey ).address, "value": int( 1e20 ) } )
account = Account.privateKeyToAccount( prkey )

def sendTrans( func, args={} ):
    args.update( {
        "from": account.address, 
        "gas": 1145141919, 
        "nonce": w3.eth.getTransactionCount( account.address ) 
    } ) 
    return w3.eth.sendRawTransaction( w3.eth.account.signTransaction( 
        func.buildTransaction( args ), private_key = prkey 
    ).rawTransaction )

def register( name ):
    fhash = hashlib.sha256( ( account.address+name ).encode( "utf8" ) ).hexdigest()
    path, chal = fhash[ :32 ], fhash[ 32: ]
    vcode = w3.eth.account.signHash( defunct_hash_message( text=chal ), private_key=prkey )
    with open( "./"+path, "wb" ) as fd:
        fd.write( vcode.signature )

    resfil = contract.events.reg_done.createFilter( fromBlock=0 )
    sendTrans( contract.functions.register( account.address, name ) )
    for _ in range( 8 ):
        time.sleep( 2 )
        if reduce( lambda S, x: S or x.args[ "addr" ]==account.address and x.args[ "domainName" ]==name, resfil.get_new_entries(), False ):
            return True
    return False
    
print( register( "www.baidu.com" ) )
sendTrans( contract.functions.modifyTrustedCAs( "GlobalSign nv-sa" ) )

