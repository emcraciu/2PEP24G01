import json
import unittest
from modul11.part3 import time_getter
from unittest.mock import patch, MagicMock

OUTPUT = ['Africa/Abidjan', 'Africa/Accra', 'Africa/Addis_Ababa', 'Africa/Algiers', 'Africa/Asmara', 'Africa/Asmera']


class TestTimeGetter(unittest.TestCase):

    @patch("modul11.part3.requests.get")
    def test_connection(self, get_mock):
        get_mock.return_value = MagicMock(text=json.dumps(OUTPUT))
        self.assertEqual(time_getter(), OUTPUT)

    # def test_with_wrong_server(self):
    #     self.assertRaises(json.decoder.JSONDecodeError, time_getter, "http://example.com")

    @patch("modul11.part3.json.loads")
    def test_payload_conversion(self, json_mock):
        json_mock.return_value = OUTPUT
        self.assertEqual(time_getter(), OUTPUT)

