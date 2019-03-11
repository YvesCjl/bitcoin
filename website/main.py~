import hashlib
from web3 import Web3, HTTPProvider, TestRPCProvider
import os

pubkey, prikey = "heyhey", "haha"
w3 = Web3( RPCProvider( host="localhost", port="8545" ) )

def register( address, name ):
    fhash = hashlib.sha256( ( address+name ).encode( "utf8" ) ).hexdigest()
    path, chal = fhash[ :32 ], fhash[ 32: ]
    vcode = w3.eth.sign( pubkey, chal.encode( "utf8" ) )
    with open( name+"/"+path, "w" ) as fd:
        fd.write( vcode )
    
register( "192.168.0.1", "D:/test" )
