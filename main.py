# main.py

import time

from blockchain.retention import RetentionPolicy
from zkp.core import create_and_verify_proof

def main():
    retention_policy = RetentionPolicy()

    # Sample transaction and retention contract
    retention_policy.add_transaction(retention_policy.create_data_retention_transaction('data_hash_1', 10, 'delete'))
    retention_policy.create_retention_contract('data_hash_1', 10, 'delete')

    # Simulate waiting to expire the retention period
    time.sleep(11)

    # Enforce data retention policies to trigger deletion
    retention_policy.enforce_data_retention_policies()

    # Generate and verify zk-STARK proof for some computation and data
    computation = "sample_computation"  # replaceable for actual computation
    data = ["data_hash_1"]  # replaceable for actual data
    zkp_result = create_and_verify_proof(computation, data)

    # Output zk-STARK proof result
    print(f"zk-STARK Proof: {zkp_result['proof']}")
    print(f"Proof Verification Result: {'Valid' if zkp_result['is_valid'] else 'Invalid'}")

    # Print audit trail
    retention_policy.audit_trail()

if __name__ == "__main__":
    main()
