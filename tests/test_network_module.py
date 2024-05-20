import unittest
import network_module

class TestNetworkModule(unittest.TestCase):
    def test_create_peer(self):
        peer = network_module.create_peer('localhost', 5000)
        self.assertIsInstance(peer, network_module.Peer)

    def test_connect_peer(self):
        peer = network_module.create_peer('localhost', 5000)
        self.assertTrue(peer.connect())

    def test_send_message(self):
        peer = network_module.create_peer('localhost', 5000)
        peer.connect()
        message = {'type': 'test', 'data': 'hello'}
        peer.send_message(message)

if __name__ == '__main__':
    unittest.main()
