import json
import boto3
from boto3.dynamodb.conditions import Key

def get_increment_view_count(action, table_name, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table(table_name)
    response = table.update_item(
        Key={'action': action},
        UpdateExpression="add view_count :inc",
        ExpressionAttributeValues={
            ':inc': 1
        },
        ReturnValues="UPDATED_NEW"
    )
    return response

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    ssm = boto3.client('ssm')
    parameter = ssm.get_parameter(Name='/www_resume/db/table_name')
    table_name = parameter['Parameter']['Value']
    response =  get_increment_view_count(0, table_name, dynamodb)
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        view_count = response['Attributes']['view_count']
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'view_count': str(view_count)
            })
        }
