pragma solidity ^0.5.0;

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
    
    
    //some constant
    uint constant auth_times = 10;
    uint constant limit_blocks = 100; // the max num of blocks to complete the auth 
    uint constant reg_fee = 0;
    uint constant verify_reward = 10;

	event reg( address addr, string domainName );
    
    //register lets domains to register themself on blockchain.
    function register(address addr, string memory domainName) public {
        //init the var to register
        reg_domain[addr].name = domainName;
        reg_domain[addr].count = 0;
        reg_domain[addr].trustCAs = "";
        reg_domain[addr].stBlock = block.number;
        reg_domain[addr].isEntity = true;
       //msg.sender 全局变量，调用合约的发起方
       //verifing_domain[verifing_domain.length] = domainName;
        emit reg( addr, domainName );
    }
    
    function report(address addr, string memory domainName, uint256 fakeVcode) public {
        //get the register blockinfo of domain
        //verify the sign of fakeVcode
        //calculate the challege
        //verify the mismatch of challenge and fakeVcode
        //reg_domain[addr].isEntity = false;
        //verifing_domain[verifing_domain.length] = domainName;
    }
    
    function verify(address addr,string memory domainName, uint256 vcode) public {
        //get the register blockinfo of domain
        //calculate the challenge
        //verify the vcode and update the progress of register
        /*auth_domain[addr].name = domainName;
        auth_domain[addr].stBlock = block.number;
        auth_domain[addr].count += 1;
        auth_domain[addr].isEntity = true;*/
        //verifing_domain[verifing_domain.length] = domainName;
        ++ reg_domain[addr].count;
    }
    
    function modifyTrustedCAs(string memory CAs) public {
        //check the progress of register
        //check the right to modify 
        string memory name = reg_domain[msg.sender].name;
        //if(keccak256(name) == keccak256("") || !auth_domain[name].isEntity) {
            //throw;
        //}
        //do action
        auth_domain[name].trustCAs = CAs;
    }
    
    function queryTrustedCAs(string memory domainName) public view returns( string memory ) {
        //return the trustCAs of queried domain
        return auth_domain[domainName].trustCAs;
    }

	function Test() public {
	}
}
