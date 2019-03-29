// certificate-info
// Copyright (C) 2017-2018 Yunzhu Li
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.
var colors = {'': '#888', 'gray': '#888', 'red': '#FF1744', 'orange': '#EF6C00'}

function fetchOwnCertInfo(hostname){
    var account = '0x67EC76aD62A83A32ecE695D5F7E9580c2E625b80'; // Dev
    var contractAddress = '0x7dd6f5b21cba0dfc0ea1de7169cedd99993e4387';

    console.log(abiArray);

    var web3 = new Web3();
    web3.setProvider(new Web3.providers.HttpProvider("http://localhost:8545"));

    web3.eth.defaultAccount = account;

    // Get hold of contract instance

    var Mycontract = web3.eth.contract(abiArray);
    var contract = Mycontract.at(contractAddress);
    console.log("calling the smart contract...");

    var ret = contract.queryTrustedCAs(hostname);
    return ret;
	//
    // return "Symantec Corporation";
}

function get_source_info(){
    //ip:port
    return "localhost:5747"
}
function get_detail(){
  return "null"
}

document.addEventListener('DOMContentLoaded', function () {
  var background = chrome.extension.getBackgroundPage();
  var currentTabId = background.currentTabId;
  var popupData = background.popupData[currentTabId];

  if (typeof popupData === 'undefined') return;

  infoFromBlockchain = fetchOwnCertInfo(popupData['hostname'])
  source = get_source_info()
  detail = get_detail()

  console.log(infoFromBlockchain)
  if(infoFromBlockchain == ''){
    infoFromBlockchain = "No Info from blcokchain."
  }
  popupData["infoFromBlockchain"] = infoFromBlockchain
  popupData["source"] = source
  popupData["detail"] = detail

  document.getElementById("infoFromBlockchain").innerHTML = popupData["infoFromBlockchain"]

  // //check
  console.log(popupData)
  if (popupData['infoFromBlockchain'] == popupData['issuer_organization']) {
    popupData['validation_result'] = "Pass!";
    popupData['result_color_hex'] = colors['orange'];
  } else {
    popupData['validation_result'] = "Not pass!";
    popupData['result_color_hex'] = colors['red'];
  }


  document.getElementById('lblValidationResult').style['background'] = popupData['result_color_hex'];
  document.getElementById('lblValidationResult').innerHTML = popupData['validation_result'];
  // document.getElementById('lblMessage').innerHTML = popupData['message'];
  document.getElementById('search_entity').innerHTML = popupData['hostname'];
  document.getElementById('source').innerHTML = popupData['source'];
  document.getElementById('detail').innerHTML = popupData['detail'];
  
  // Identity
  if (popupData["subject_organization"].length > 0) {
    document.getElementById('lblSubjectOrganization').innerHTML = popupData['subject_organization'];
  } else {
    document.getElementById('lblSubjectOrganization').innerHTML = '';
  }

  // Issuer
  if (popupData["issuer_common_name"].length > 0) {
    document.getElementById('pIssuer').style['display'] = 'block';
    document.getElementById('lblIssuerOrganization').innerHTML = '<b>' + popupData['issuer_organization'] + '</b>';
    document.getElementById('lblIssuerCommonName').innerHTML = popupData['issuer_common_name'];
  } else {
    document.getElementById('pIssuer').style['display'] = 'none';
  }
});
