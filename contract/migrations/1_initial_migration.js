const Migrations = artifacts.require("Migrations");
//const Contract = artifacts.require("contract.sol");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
  //deployer.deploy(contract);
};
