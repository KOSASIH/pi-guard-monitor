import unittest
import identity_module

class TestIdentityModule(unittest.TestCase):
    def test_create_identity(self):
        identity = identity_module.create_identity()
        self.assertIsInstance(identity, identity_module.Identity)

    def test_load_identity(self):
        identity = identity_module.create_identity()
        identity.save_identity('test_identity.json')
        loaded_identity = identity_module.load_identity('test_identity.json')
        self.assertIsInstance(loaded_identity, identity_module.Identity)

    def test_unlock_identity(self):
        identity = identity_module.create_identity()
        identity.save_identity('test_identity.json')
        loaded_identity = identity_module.load_identity('test_identity.json')
        self.assertTrue(loaded_identity.unlock_identity('passphrase'))

if __name__ == '__main__':
    unittest.main()
