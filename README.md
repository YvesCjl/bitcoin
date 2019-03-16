# PKI

## automatic runs

./run.sh

## ~~Steps to run~~

terminal 1: ganache-cli -l 10000000000 -e 10000000000

terminal 2: cd contract; truffle migrate

terminal 3: cd verifier; edit main.py with contract address; python main.py

terminal 4: cd website; edit main.py with contract address; python main.py

## Contract

./contract truffle files

./contract/contracts/contract.sol the PKI contract

./contract/build/contracts/MyContract.sol interface for truffle

./contract/migration/2\_deploy\_contract.js interface for contract deployment

## website client

./website/main.py client python code

## verifier client

./verifier/main.py client python code


