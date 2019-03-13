pragma solidity ^0.4.21;

contract MyContract {
    
    struct Domain {
        string name;   //域名名称
        uint count;    //验证次数
        string trustCAs;  //信任CA
        uint stBlock;  //验证开始的区块
        address[] validator;  //验证者列表
        bool isEntity; // as a flag for existence
    }
    
    mapping(address => Domain) reg_domain;  //待认证域名
    mapping(string => Domain)  auth_domain; //已认证域名
    mapping (address => uint) balances;     //余额
    string[] verifing_domain;
    mapping(string => uint) mapForId;
    
    
    //some constant
    uint constant auth_times = 10;
    uint constant limit_blocks = 100; // the max num of blocks to complete the auth 
    uint constant reg_fee = 0;
    uint constant verify_reward = 10;

	event register( address addr, string domainName );
    
    //register lets domains to register themself on blockchain.
    function register(address addr, string domainName) {
        //init the var to register
        reg_domain[addr].name = domainName;
        reg_domain[addr].count = 0;
        reg_domain[addr].trustCAs = "";
        reg_domain[addr].stBlock = block.number;
        reg_domain[addr].isEntity = true;
        balances[msg.sender] -= reg_fee;
        //msg.sender 全局变量，调用合约的发起方
        verifing_domain[verifing_domain.length] = domainName;
		emit register( addr, domainName );
    }
    
    function report(address addr, string domainName, uint256 fakeVcode) {
        //get the register blockinfo of domain
        //verify the sign of fakeVcode
        //calculate the challege
        //verify the mismatch of challenge and fakeVcode
        reg_domain[addr].isEntity = false;
        balances[msg.sender] += verify_reward/2;
        balances[addr] -= reg_fee;
        verifing_domain[verifing_domain.length] = domainNxame;

    }
    
    function verify(address addr,string domainName, uint256 vcode) {
        //get the register blockinfo of domain
        //calculate the challenge
        //verify the vcode and update the progress of register
        auth_times -= 1;
        auth_domain[addr].name = domainName;
        auth_domain[addr].stBlock = block.number;
        auth_domain[addr].count += 1;
        auth_domain[addr].validator[mapForId] = this.addr;
        auth_domain[addr].isEntity = true;
        verifing_domain[verifing_domain.length] = domainName;
    }
    
    function modifyTrustedCAs(string CAs) {
        //check the progress of register
        //check the right to modify 
        string name = reg_domain[msg.sender].name;
        if(keccak256(name) == keccak256("") || !auth_domain[name].isEntity) {
            throw() ;
        }
        //do action
        auth_domain[name].trustCAs = CAs;
    }
    
    function queryTrustedCAs(string domainName) public view returns(string) {
        //return the trustCAs of queried domain
        return auth_domain[domainName].trustCAs;
    }
}
