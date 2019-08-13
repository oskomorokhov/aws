#import boto3
import json
#import os

print('Loading function')
#dynamo = boto3.client('dynamodb')
#table_name = os.environ['TABLE_NAME']

functions = {
    '/test' : '/test',
    '/test/' : '/test/',
    '/Dev' : '/Dev',
    '/Dev/' : '/Dev/',
    '/Dev/test' : '/Dev/test',
    '/Dev/test/' : '/Dev/test/',
    '/Stage' : '/Stage',
    '/Stage/' : '/Stage/',
    '/Stage/test' : '/Stage/test',
    '/Stage/test/' : '/Stage/test/',
    '/Prod' : '/Prod',
    '/Prod/' : '/Prod/',
    '/Prod/test' : '/Prod/test',
    '/Prod/test/' : '/Prod/test/',
    '/' : 'root (/)'

}

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.
	TableName provided by template.yaml.
    To scan a DynamoDB table, make a GET request with optional query string parameter.
	To put, update, or delete an item, make a POST, PUT, or DELETE request respectively,
	passing in the payload to the DynamoDB API as a JSON body.
        operations = {
            'DELETE': lambda dynamo, x: dynamo.delete_item(TableName=table_name, **x),
    		'GET': lambda dynamo, x: dynamo.scan(TableName=table_name, **x) if x else dynamo.scan(TableName=table_name),
            'POST': lambda dynamo, x: dynamo.put_item(TableName=table_name, **x),
            'PUT': lambda dynamo, x: dynamo.update_item(TableName=table_name, **x),
        }

        operation = event['httpMethod']
        if operation in operations:
            payload = event['queryStringParameters'] if operation == 'GET' else json.loads(event['body'])
            return respond(None, operations[operation](dynamo, payload))
        else:
            return respond(ValueError('Unsupported method "{}"'.format(operation)))
    '''

    print("Received event: " + json.dumps(event, indent=2))


    print(event)

    function = event['path']
    payload=functions[function]

    return respond(None, payload)
