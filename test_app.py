import unittest
import app

class TestCurrencyAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()  # Используем app.app для обращения к Flask приложению
        self.app.testing = True

    def test_currency_rate(self):
        response = self.app.post('/currency', json={'currency': 'USD'})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('rate_to_rub', data)

if __name__ == '__main__':
    unittest.main()
