# blockchain/core.py

import time as time

from retention import RetentionPolicy

def main():
    retention_policy = RetentionPolicy()

    # sample transaction
    retention_policy.add_transaction(retention_policy.create_data_retention_transaction('data_hash_1', 
                                                                                        10, 
                                                                                        'delete'))

    # retention contract
    retention_policy.create_retention_contract('data_hash_1', 
                                               10, 
                                               'delete')

    # Simulate waiting for some time
    time.sleep(11)

    # Enforce data retention policies, where this triggers deletion
    retention_policy.enforce_data_retention_policies()

    # audit trail
    retention_policy.audit_trail()

if __name__ == "__main__":
    main()
