var abiArray = [
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
			}
		],
		"name": "report",
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
				"name": "index",
				"type": "uint256"
			}
		],
		"name": "get_verifing_domain_name_by_index",
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
		"constant": true,
		"inputs": [],
		"name": "get_verifing_domain_num",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
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
		"constant": true,
		"inputs": [
			{
				"name": "name",
				"type": "string"
			}
		],
		"name": "show_auth",
		"outputs": [
			{
				"name": "name1",
				"type": "string"
			},
			{
				"name": "addr",
				"type": "address"
			},
			{
				"name": "count",
				"type": "uint256"
			},
			{
				"name": "CAs",
				"type": "string"
			},
			{
				"name": "num",
				"type": "uint256"
			},
			{
				"name": "isEntity",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "addr",
				"type": "address"
			}
		],
		"name": "show_verify",
		"outputs": [
			{
				"name": "name",
				"type": "string"
			},
			{
				"name": "addr1",
				"type": "address"
			},
			{
				"name": "count",
				"type": "uint256"
			},
			{
				"name": "CAs",
				"type": "string"
			},
			{
				"name": "num",
				"type": "uint256"
			},
			{
				"name": "isEntity",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
];

module.exports = function () {
	return abiArray;
}