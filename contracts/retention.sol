// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./oracleManager.sol";

contract RetentionPolicy {
    struct RetentionContract {
        uint256 createdAt;
        uint256 retentionPeriod;
        bool deleted;
    }

    mapping(bytes32 => RetentionContract) public retentionContracts;
    OracleManager public oracleManager;

    event DataDeleted(bytes32 indexed dataHash);

    constructor(address _oracleManager) {   
        oracleManager = OracleManager(_oracleManager);
    }

    function createRetentionContract(bytes32 dataHash, uint256 retentionPeriod) external {
        retentionContracts[dataHash] = RetentionContract({
            createdAt: block.timestamp,
            retentionPeriod: retentionPeriod,
            deleted: false
        });
    }

    function enforceDataRetentionPolicies() external {
        for (bytes32 dataHash in retentionContracts) {
            if (!retentionContracts[dataHash].deleted && isRetentionPeriodExpired(dataHash)) {
                bool consensusDecision = oracleManager.getConsensus(dataHash);
                if (consensusDecision) {
                    deleteData(dataHash);
                }
            }
        }
    }

    function isRetentionPeriodExpired(bytes32 dataHash) internal view returns (bool) {
        return (block.timestamp - retentionContracts[dataHash].createdAt) > retentionContracts[dataHash].retentionPeriod;
    }

    function deleteData(bytes32 dataHash) internal {
        retentionContracts[dataHash].deleted = true;
        emit DataDeleted(dataHash);
    }
}
