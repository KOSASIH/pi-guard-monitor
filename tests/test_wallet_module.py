import unittest
import wallet_module

class TestWalletModule(unittest.TestCase):
    def test_create_wallet(self):
        wallet = wallet_module.create_wallet()
        self.assertIsInstance(wallet, wallet_module.Wallet)

    def test_get_address(self):
        wallet = wallet_module.create_wallet()
        address = wallet.get_address()
        self.assertIsInstance(address, str)

    def test_get_private_key(self):
        wallet = wallet_module.create_wallet()
        private_key = wallet.get_private_key()
        self.assertIsInstance(private_key, str)

if __name__ == '__main__':
    unittest.main()
