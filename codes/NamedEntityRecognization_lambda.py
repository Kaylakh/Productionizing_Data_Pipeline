import os, zipfile
from io import BytesIO
import boto3
import logging 
import json

s3 = boto3.client('s3')
client = boto3.client('comprehend')

def lambda_handler(event, context):
    bucket = 'assign2-scrape-bucket'
    key = event['key']
    decision = event['decision']
    
    # generate new key name
    new_key = "EntityExtractionOutput/%s.txt" % os.path.basename(key)
    # read the source obj content
    body = s3.get_object(Bucket=bucket, Key=key)['Body'].read().decode()
    

    try:
        entities_response = client.detect_entities(Text=body, LanguageCode='en')
        entity_list = entities_response['Entities']
        print ('entity extraction completed')
        print(entity_list)
        
    except Exception as e:
        logging.error('Exception: %s. Unable to extract entities from message' % e)
        raise e
    upload_byte_stream = bytes(json.dumps(entity_list).encode('UTF-8'))
    s3.put_object(Bucket = bucket, Body = upload_byte_stream, Key= new_key)
    response = {'data': body, 'entities': entity_list, 'decision' : decision}
    return response