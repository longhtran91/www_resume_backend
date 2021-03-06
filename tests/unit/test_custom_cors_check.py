import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import unittest
from app.custom_cors_check import custom_cors_check as CCC

class CustomCORSCheck(unittest.TestCase):
    def setUp(self):
        self.origin = 'resume.lhtran.com'
        self.test_api_event = {
            'headers': {
                'origin': self.origin
            }
        }

    def test_CustomCORSCheck_1(self):
        result = CCC.lambda_handler(event=self.test_api_event, context={})

        self.assertEqual(result, {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Access-Control-Allow-Methods': 'GET,POST,OPTIONS',
                'Access-Control-Allow-Origin': self.origin
            }
        })

if __name__ == '__main__':
    unittest.main()