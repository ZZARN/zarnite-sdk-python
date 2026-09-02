import unittest

from zarnite.client import Zarnite, ZarniteError


class TestSmokeClient(unittest.TestCase):
    def test_client_initializes_core_services(self) -> None:
        client = Zarnite(api_key="zar_test_smoke")

        self.assertEqual(client.configuration.host, "https://api.zarnite.com")
        self.assertIsNotNone(client.agents)
        self.assertIsNotNone(client.knowledge)
        self.assertIsNotNone(client.voice_runtime)

    def test_client_requires_api_key(self) -> None:
        with self.assertRaises(ZarniteError):
            Zarnite(api_key="")


if __name__ == "__main__":
    unittest.main()
