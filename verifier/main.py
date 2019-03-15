import hashlib
import json
import time
from eth_account import Account
from eth_account.messages import defunct_hash_message
from web3 import Web3, HTTPProvider, TestRPCProvider
import os

w3 = Web3( HTTPProvider( "http://127.0.0.1:8545" ) )
w3.eth.defaultAccount = w3.eth.accounts[-2]
contract = w3.eth.contract( address=open( "../contract/contract_address", "r" ).read().strip( '\n' ), abi=json.load( open( "../contract/contracts/contract.abi", "r" ) ) )

try:
    prkey = Account.decrypt( json.load( open( "./.keystore/key", "r" ) ), "123" )
except:
    prkey = Account.create().privateKey
    json.dump( Account.encrypt( prkey, "123" ), open( "./.keystore/key", "w" ) )
    w3.eth.sendTransaction( transaction={ "from": w3.eth.accounts[-2], "to": Account.privateKeyToAccount( prkey ).address, "value": int( 1e7 ) } )
account = Account.privateKeyToAccount( prkey )

def verify( address, name ):
    fhash = hashlib.sha256( ( address+name ).encode( "utf8" ) ).hexdigest()
    path, chal = fhash[ :32 ], fhash[ 32: ]
    try:
        fd = open( "../website/"+path, "rb" )
        if w3.eth.account.recoverHash( defunct_hash_message( text=chal ), signature=fd.read() )==address:
            print( "Verify passed!" )
            return True
    except:
        print( "Failed!" )
        return False

evefil = contract.events.reg.createFilter( fromBlock=0 )
while True: 
    for event in evefil.get_new_entries():
        if verify( event.args[ "addr" ], event.args[ "domainName" ] ):
            pass
        else:
            pass
    time.sleep( 5 )
    #print( w3.eth.account.recoverHash( defunct_hash_message( text=chal ), signature=vcode.signature ) )
    #contract.functions.Test().call()
    #contract.functions.verify( account.address, name ).transact( transaction={ "gas":1145141919 } )
    #print( account.address )
	
