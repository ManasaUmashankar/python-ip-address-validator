
import unittest

from src.validator import validate_ip


class TestIPValidator(unittest.TestCase):

    def test_valid_ipv4(self):
        result = validate_ip("192.168.1.1")
        self.assertTrue(result["valid"])
        self.assertEqual(result["version"], 4)

    def test_valid_ipv6(self):
        result = validate_ip("2001:4860:4860::8888")
        self.assertTrue(result["valid"])
        self.assertEqual(result["version"], 6)

    def test_invalid_ip(self):
        result = validate_ip("999.999.999.999")
        self.assertFalse(result["valid"])

    def test_private_ip(self):
        result = validate_ip("192.168.1.1")
        self.assertEqual(result["type"], "Private")

    def test_public_ip(self):
        result = validate_ip("8.8.8.8")
        self.assertEqual(result["type"], "Public")

    def test_loopback_ip(self):
        result = validate_ip("127.0.0.1")
        self.assertEqual(result["type"], "Loopback")

    def test_multicast_ip(self):
        result = validate_ip("224.0.0.1")
        self.assertEqual(result["type"], "Multicast")


if __name__ == "__main__":
    unittest.main()
