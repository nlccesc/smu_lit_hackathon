# blockchain/marketplace.py

import time as time

from blockchain import Blockchain


class DataMarketplace(Blockchain):
    def __init__(self):
        super().__init__(permissioned=True)
        self.marketplace_transactions = []

    def list_data(self, 
                  data_owner: str, 
                  data_hash: str, 
                  price: float):
        if self.validate_transaction({'data_owner': data_owner}):
            self.marketplace_transactions.append({
                'data_owner': data_owner,
                'data_hash': data_hash,
                'price': price,
                'timestamp': time(),
                'status': 'listed'
            })

    def purchase_data(self, 
                      buyer: str, 
                      data_hash: str):
        for transaction in self.marketplace_transactions:
            if transaction['data_hash'] == data_hash and transaction['status'] == 'listed':
                transaction['buyer'] = buyer
                transaction['status'] = 'sold'
                print(f"Data {data_hash} purchased by {buyer}")
                return transaction
        print(f"Data {data_hash} not available or already sold")

