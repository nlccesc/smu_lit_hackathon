# blockchain/transactions.py

from blockchain.blockchain import Blockchain
from time import time
from typing import List, Dict, Any


class Transactions(Blockchain):
    def create_consent_transaction(self, 
                                   data_owner: str, 
                                   data_elements: List[str], 
                                   processing_activities: List[str], 
                                   consent_given: bool) -> Dict[str, Any]:
        return {
            'data_owner': data_owner,
            'data_elements': data_elements,
            'processing_activities': processing_activities,
            'consent_given': consent_given,
            'timestamp': time(),
            'gdpr_compliance': True
        }

    def create_data_retention_transaction(self, 
                                          data_hash: str, 
                                          retention_period: int, 
                                          deletion_action: str) -> Dict[str, Any]:
        return {
            'data_hash': data_hash,
            'retention_period': retention_period,
            'deletion_action': deletion_action,
            'timestamp': time(),
            'gdpr_compliance': True
        }

    def create_model_training_transaction(self, 
                                          model_id: str, 
                                          training_data_hash: str, 
                                          model_params_hash: str) -> Dict[str, Any]:
        return {
            'model_id': model_id,
            'training_data_hash': training_data_hash,
            'model_params_hash': model_params_hash,
            'timestamp': time(),
            'event_type': 'model_training'
        }

    def create_model_decision_transaction(self, 
                                          model_id: str, 
                                          input_data_hash: str, 
                                          decision_output: str) -> Dict[str, Any]:
        return {
            'model_id': model_id,
            'input_data_hash': input_data_hash,
            'decision_output': decision_output,
            'timestamp': time(),
            'event_type': 'model_decision'
        }

