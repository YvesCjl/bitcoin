import hashlib
import json
import time
from hexbytes import HexBytes
from eth_account import Account
from eth_account.messages import defunct_hash_message
from web3 import Web3, HTTPProvider, TestRPCProvider
import os

w3 = Web3( HTTPProvider( "http://127.0.0.1:8545" ) )
contract = w3.eth.contract( address=open( "../contract/contract_address", "r" ).read().strip( '\n' ), abi=json.load( open( "../contract/contracts/contract.abi", "r" ) ) )

try:
    prkey = Account.decrypt( json.load( open( "./.keystore/key", "r" ) ), "123" )
except:
    prkey = Account.create().privateKey
    json.dump( Account.encrypt( prkey, "123" ), open( "./.keystore/key", "w" ) )

w3.eth.sendTransaction( transaction={ "from": w3.eth.accounts[-2], "to": Account.privateKeyToAccount( prkey ).address, "value": int( 1e20 ) } )
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

def verify( address, name ):
    fhash = hashlib.sha256( ( address+name ).encode( "utf8" ) ).hexdigest()
    path, chal = fhash[ :32 ], fhash[ 32: ]
    #try:
    sig = open( "../website/"+path, "rb" ).read()
    if w3.eth.account.recoverHash( defunct_hash_message( text=chal ), signature=sig )==address:
        print( "Verify passed!" )
        sendTrans( contract.functions.verify( address, name, 0 ) )
    #except:
    #    print( "Failed!" )

evefil = contract.events.reg.createFilter( fromBlock=0 )
while True: 
    list( map( lambda x: verify( x.args[ "addr" ], x.args[ "domainName" ] ), evefil.get_new_entries() ) )
    '''
    for event in evefil.get_new_entries():
        verify( event.args[ "addr" ], event.args[ "domainName" ] )
    '''
    time.sleep( 5 )
    #print( w3.eth.account.recoverHash( defunct_hash_message( text=chal ), signature=vcode.signature ) )
    #contract.functions.Test().call()
    #contract.functions.verify( account.address, name ).transact( transaction={ "gas":1145141919 } )
    #print( account.address )
	




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
    
register( "www.baidu.com" )
sendTrans( contract.functions.modifyTrustedCAs( "PKU" ) )
