import hashlib
import json
from eth_account import Account
from eth_account.messages import defunct_hash_message
from web3 import Web3, HTTPProvider, TestRPCProvider
import os

#pubkey, prikey = "0xfddc805618a38ae13505484aac9836145629cd40", "0x975edafe28d749aec9cd83b1b018bf19e529218384f96f4780f9e4577f13a67d"
w3 = Web3( HTTPProvider( "http://127.0.0.1:8545" ) )
w3.eth.defaultAccount = w3.eth.accounts[-1]
contract = w3.eth.contract( address="0x6d4b0c6399E33fF225a55B9aA42cfa19ED1D0AB6", abi=json.load( open( "../contract/contracts/contract.abi", "r" ) ) )

try:
	prkey = Account.decrypt( json.load( open( "./.keystore/key", "r" ) ), "123" )
except:
	prkey = Account.create().privateKey
	json.dump( Account.encrypt( prkey, "123" ), open( "./.keystore/key", "w" ) )
account = Account.privateKeyToAccount( prkey )

def register( name ):
    fhash = hashlib.sha256( ( account.address+name ).encode( "utf8" ) ).hexdigest()
    path, chal = fhash[ :32 ], fhash[ 32: ]
    vcode = w3.eth.account.signHash( defunct_hash_message( text=chal ), private_key=prkey )
    with open( "./"+path, "w" ) as fd:
        fd.write( str( vcode ) )
    contract.functions.Test().call()
    contract.functions.register( w3.eth.accounts[-1], name ).transact( transaction={ "from": w3.eth.accounts[-1],  "gas":1145141919 } )
	
register( "www.baidu.com" )
