// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Oracle {
    address public oracleManager;
    address public owner;

    event DataProvided(bytes32 indexed dataHash, bool decision);

    constructor(address _oracleManager) {
        oracleManager = _oracleManager;
        owner = msg.sender;
    }

    modifier onlyManager() {
        require(msg.sender == oracleManager, "Not authorized");
        _;
    }

    function provideData(bytes32 dataHash, bool decision) external onlyManager {
        emit DataProvided(dataHash, decision);
    }
}
