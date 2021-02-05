import json, re

def domain_check(url):
    DOMAIN_REGEX = r'(.*\.)?lhtran\.com.*'
    if (re.search(DOMAIN_REGEX, url)):
        return True
    else:
        return False

def lambda_handler(event, context):
    url = event['headers']['origin']
    if (domain_check(url)):
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Access-Control-Allow-Methods': 'GET,POST,OPTIONS',
                'Access-Control-Allow-Origin': url
            }
        }
