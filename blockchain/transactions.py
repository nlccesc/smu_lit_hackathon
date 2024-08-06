# blockchain/transactions.py

from blockchain.blockchain import Blockchain
from time import time
from typing import (
    List, Dict, Any, TypeVar
)

S = TypeVar('S', bound=str)
LS = TypeVar('LS', bound=List[str])

class Transactions(Blockchain):
    def create_consent_transaction(self, 
                                   data_owner: S, 
                                   data_elements: LS, 
                                   processing_activities: LS, 
                                   consent_given: bool) -> Dict[S, Any]:
        return {
            'data_owner': data_owner,
            'data_elements': data_elements,
            'processing_activities': processing_activities,
            'consent_given': consent_given,
            'timestamp': time(),
            'gdpr_compliance': True
        }

    def create_data_retention_transaction(self, 
                                          data_hash: S, 
                                          retention_period: int, 
                                          deletion_action: S) -> Dict[S, Any]:
        return {
            'data_hash': data_hash,
            'retention_period': retention_period,
            'deletion_action': deletion_action,
            'timestamp': time(),
            'gdpr_compliance': True
        }

    def create_model_training_transaction(self, 
                                          model_id: S, 
                                          training_data_hash: S, 
                                          model_params_hash: S) -> Dict[S, Any]:
        return {
            'model_id': model_id,
            'training_data_hash': training_data_hash,
            'model_params_hash': model_params_hash,
            'timestamp': time(),
            'event_type': 'model_training'
        }

    def create_model_decision_transaction(self, 
                                          model_id: S, 
                                          input_data_hash: S, 
                                          decision_output: S) -> Dict[S, Any]:
        return {
            'model_id': model_id,
            'input_data_hash': input_data_hash,
            'decision_output': decision_output,
            'timestamp': time(),
            'event_type': 'model_decision'
        }


