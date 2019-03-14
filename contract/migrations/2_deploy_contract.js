var Mycon = artifacts.require( "MyContract" )
module.exports=function(deployer)
{
    deployer.deploy(Mycon);
}
