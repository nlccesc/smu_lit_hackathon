// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./oracle.sol";

contract OracleManager {
    address[] public oracles;
    mapping(bytes32 => bool[]) public oracleDecisions;
    uint256 public consensusThreshold;

    event ConsensusReached(bytes32 indexed dataHash, bool consensusDecision);

    constructor(address[] memory _oracles, uint256 _threshold) {
        oracles = _oracles;
        consensusThreshold = _threshold;
    }

    function receiveOracleDecision(bytes32 dataHash, bool decision) external {
        require(isOracle(msg.sender), "Only registered oracles can submit data");
        oracleDecisions[dataHash].push(decision);

        if (oracleDecisions[dataHash].length == oracles.length) {
            bool consensusDecision = getConsensus(dataHash);
            emit ConsensusReached(dataHash, consensusDecision);
        }
    }

    function isOracle(address _oracle) internal view returns (bool) {
        for (uint256 i = 0; i < oracles.length; i++) {
            if (oracles[i] == _oracle) {
                return true;
            }
        }
        return false;
    }

    function getConsensus(bytes32 dataHash) internal view returns (bool) {
        uint256 countTrue = 0;
        for (uint256 i = 0; i < oracleDecisions[dataHash].length; i++) {
            if (oracleDecisions[dataHash][i]) {
                countTrue++;
            }
        }
        return countTrue >= consensusThreshold;
    }
}
