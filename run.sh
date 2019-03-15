echo set up ganache
ganache-cli -e 1000000000 -l 10000000000 > contract/ganache.log &
sleep 5
echo migrate contract
cd contract
truffle migrate | grep -A 4 MyContract | grep address | grep -o -e 0x.* > contract_address
cd ..
sleep 5
echo start verifier
cd verifier
python main.py &
cd ..
sleep 5
echo start register
cd website
python main.py
cd ..

