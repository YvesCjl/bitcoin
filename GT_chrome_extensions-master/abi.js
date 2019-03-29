var abiArray = [
	{
		"constant": false,
		"inputs": [
			{
				"name": "addr",
				"type": "address"
			},
			{
				"name": "domainName",
				"type": "string"
			}
		],
		"name": "register",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "addr",
				"type": "address"
			},
			{
				"name": "domainName",
				"type": "string"
			},
			{
				"name": "vcode",
				"type": "uint256"
			}
		],
		"name": "verify",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "domainName",
				"type": "string"
			}
		],
		"name": "queryTrustedCAs",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "Test",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "CAs",
				"type": "string"
			}
		],
		"name": "modifyTrustedCAs",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "addrVer",
				"type": "address"
			},
			{
				"name": "addrWeb",
				"type": "address"
			},
			{
				"name": "domainName",
				"type": "string"
			}
		],
		"name": "report",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "addr",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "domainName",
				"type": "string"
			}
		],
		"name": "reg",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "addr",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "domainName",
				"type": "string"
			}
		],
		"name": "reg_done",
		"type": "event"
	}
];

module.exports = function () {
	return abiArray;
}
