import unittest
import blockchain_module

class TestBlockchainModule(unittest.TestCase):
    def test_create_blockchain(self):
        blockchain = blockchain_module.create_blockchain()
        self.assertIsInstance(blockchain, blockchain_module.Blockchain)

    def test_add_block(self):
        blockchain = blockchain_module.create_blockchain()
        blockchain.add_block('transaction data')
        self.assertEqual(len(blockchain.chain), 2)

    def test_validate_chain(self):
        blockchain = blockchain_module.create_blockchain()
        blockchain.add_block('transaction data')
        self.assertTrue(blockchain.validate_chain())

if __name__ == '__main__':
    unittest.main()
