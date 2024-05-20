# blockchain_module.py

import logging
import requests

class BlockchainModule:
    def __init__(self, config):
        self.logger = logging.getLogger(__name__)
        self.config = config
        self.rpc_url = config['blockchain']['rpc_url']
        self.api_key = config['blockchain']['api_key']

    def get_blockchain_info(self):
        # Implement blockchain info retrieval here
        self.logger.info('Retrieving blockchain info...')
        headers = {'X-API-Key': self.api_key}
        response = requests.get(f'{self.rpc_url}/blockchain/info', headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            self.logger.error(f'Failed to retrieve blockchain info: {response.text}')
            return None

    def get_transaction_info(self, txid):
        # Implement transaction info retrieval here
        self.logger.info(f'Retrieving transaction info for txid: {txid}...')
        headers = {'X-API-Key': self.api_key}
        response = requests.get(f'{self.rpc_url}/blockchain/transaction/info/{txid}', headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            self.logger.error(f'Failed to retrieve transaction info for txid: {txid}: {response.text}')
            return None
