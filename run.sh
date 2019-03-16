echo set up ganache
ganache-cli -e 1000000000 -l 10000000000 > contract/ganache.log &
sleep 4
echo migrate contract
cd contract
truffle migrate | grep -A 4 MyContract | grep address | grep -o -e 0x.* > contract_address
cd ..
echo start verifier
cd verifier
python main.py & > client.log
cd ..
sleep 1
echo start register
cd website
python main.py > client.log
cd ..

