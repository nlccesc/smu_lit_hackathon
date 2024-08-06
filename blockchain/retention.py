# blockchain/retention.py

from transactions import Transactions
import time
from typing import Dict, Any


class RetentionPolicy(Transactions):
    def __init__(self):
        super().__init__()
        self.retention_contracts: Dict[str, Dict[str, Any]] = {}

    def create_retention_contract(self, 
                                  data_hash: str, 
                                  retention_period: int, 
                                  deletion_action: str):
        contract = {
            'data_hash': data_hash,
            'retention_period': retention_period,
            'deletion_action': deletion_action,
            'created_at': time.time(),
            'immutable': True,
            'audit_trail': self.add_transaction(self.create_data_retention_transaction(data_hash, 
                                                                                       retention_period, 
                                                                                       deletion_action))
        }
        self.retention_contracts[data_hash] = contract
        print(f"Retention contract created for data hash {data_hash}")

    def is_retention_period_expired(self, contract: Dict[str, Any]) -> bool:
        return (time.time() - contract['created_at']) > contract['retention_period']

    def execute_deletion_action(self, contract: Dict[str, Any]):
        print(f"Executing deletion action for data hash: {contract['data_hash']}")
        print(f"Data with hash {contract['data_hash']} has been deleted as per the smart contract.")

    def enforce_data_retention_policies(self):
        expired_contracts = []

        for data_hash, contract in self.retention_contracts.items():
            if self.is_retention_period_expired(contract):
                self.execute_deletion_action(contract)
                expired_contracts.append(data_hash)

        # Remove contracts after deletion
        for data_hash in expired_contracts:
            del self.retention_contracts[data_hash]
            print(f"Retention contract for data hash {data_hash} has been removed.")

    def audit_trail(self):
        # Simulate an audit trail, listing all retention contracts and their statuses
        print("Audit Trail:")
        for data_hash, contract in self.retention_contracts.items():
            print(f"Data Hash: {data_hash}, 
                  Created At: {contract['created_at']}, 
                  Retention Period: {contract['retention_period']}, 
                  Deletion Action: {contract['deletion_action']}, 
                  Expired: {self.is_retention_period_expired(contract)}")


