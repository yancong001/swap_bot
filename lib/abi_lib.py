import json
EIP20_ABI = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],'
                       '"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{'
                       '"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve",'
                       '"outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable",'
                       '"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"",'
                       '"type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},'
                       '{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to",'
                       '"type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{'
                       '"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},'
                       '{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],'
                       '"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{'
                       '"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"",'
                       '"type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},'
                       '{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],'
                       '"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{'
                       '"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer",'
                       '"outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable",'
                       '"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},'
                       '{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"",'
                       '"type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},'
                       '{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},'
                       '{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value",'
                       '"type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{'
                       '"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender",'
                       '"type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval",'
                       '"type":"event"}]')
BEP_ABI = json.loads("""[ { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", 
"name": "owner", "type": "address" }, { "indexed": true, "internalType": "address", "name": "spender", 
"type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], 
"name": "Approval", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": 
"address", "name": "from", "type": "address" }, { "indexed": true, "internalType": "address", "name": "to", 
"type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], 
"name": "Transfer", "type": "event" }, { "constant": true, "inputs": [ { "internalType": "address", "name": "_owner", 
"type": "address" }, { "internalType": "address", "name": "spender", "type": "address" } ], "name": "allowance", 
"outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "payable": false, "stateMutability": 
"view", "type": "function" }, { "constant": false, "inputs": [ { "internalType": "address", "name": "spender", 
"type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "approve", 
"outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "payable": false, "stateMutability": 
"nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "internalType": "address", "name": "account", 
"type": "address" } ], "name": "balanceOf", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } 
], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], 
"name": "decimals", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "payable": false, 
"stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "getOwner", "outputs": [ { 
"internalType": "address", "name": "", "type": "address" } ], "payable": false, "stateMutability": "view", 
"type": "function" }, { "constant": true, "inputs": [], "name": "name", "outputs": [ { "internalType": "string", 
"name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": 
true, "inputs": [], "name": "symbol", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], 
"payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], 
"name": "totalSupply", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "payable": false, 
"stateMutability": "view", "type": "function" }, { "constant": false, "inputs": [ { "internalType": "address", 
"name": "recipient", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], 
"name": "transfer", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "payable": false, 
"stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "internalType": "address", 
"name": "sender", "type": "address" }, { "internalType": "address", "name": "recipient", "type": "address" }, 
{ "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "transferFrom", "outputs": [ { 
"internalType": "bool", "name": "", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", 
"type": "function" } ]""")