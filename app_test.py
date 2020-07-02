import app
import unittest

class TestIndex(unittest.TestCase):
    
    def SetUp(self):
        self.app = app.app.test_client()
    
    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__': 
    unittest.main()