import unittest
import boto3
from moto import mock_dynamodb2
import view_count as ViewCount

def create_table(table_name, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url='http://localhost:8000')

    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'action',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'action',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )
    table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
    assert table.table_status == 'ACTIVE'
    return table
    
def initialize_data(table_name, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table(table_name)
    response = table.put_item(
        Item={
                'action': 0,
                'view_count': 0
            }
    )

@mock_dynamodb2
class GetViewCountTest(unittest.TestCase):
    
    def setUp(self):
        """
        Create database resource and mock table
        """
        self.table_name = 'www_resume'
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        self.table = create_table(table_name = self.table_name, dynamodb = self.dynamodb)
        initialize_data(table_name = self.table_name, dynamodb = self.dynamodb)

    def tearDown(self):
        """
        Delete database resource and mock table
        """
        self.table.delete()
        self.dynamodb=None
    
    def test_table_exists(self):
        """
        Test if our mock table is ready
        """
        self.assertTrue(self.table)
        self.assertIn(self.table_name, self.table.name)

    def test_GetIncrementViewCount_1(self):
        response = ViewCount.get_increment_view_count(0, self.table_name, self.dynamodb)
        self.assertEqual(200, response['ResponseMetadata']['HTTPStatusCode'])


if __name__ == '__main__':
    unittest.main()