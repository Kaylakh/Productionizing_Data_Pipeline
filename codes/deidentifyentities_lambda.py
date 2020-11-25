import hashlib
import base64
import logging
import uuid
import boto3
import json

s3=boto3.client('s3')
ddb = boto3.client('dynamodb')

def timeout(event, context):
    raise Exception('Execution is about to time out, exiting...')
    
def store_deidentified_message(message, entity_map, ddb_table):
    hashed_message = hashlib.sha3_256(message.encode()).hexdigest()
    for entity_hash in entity_map:
        ddb.put_item(
            TableName=ddb_table,
            Item={
                'EntityHash': {
                    'S': entity_hash
                },
                'Hash_Message': {
                    'S': hashed_message
                },
                'Entity': {
                    'S': entity_map[entity_hash]
                }
            }
        )
    return hashed_message
    
def deidentify_entities_in_message(message, entity_list):
    entity_map = dict()
    for entity in entity_list:
      salted_entity = entity['Text'] + str(uuid.uuid4())
      hashkey = hashlib.sha3_256(salted_entity.encode()).hexdigest()
      entity_map[hashkey] = entity['Text']
      message = message.replace(entity['Text'], hashkey)
    return message, entity_map
    
def lambda_handler(event, context):
    bucket = 'assign2-scrape-bucket'
    try:
        # Extract the entities and message from the event
        #originalDataObject= s3.get_object(Bucket = bucket, Key= 'ScrapedFolder/webscrape.txt')
        #Entityobject= s3.get_object(Bucket = bucket, Key= 'EntityExtractionOutput/webscrape.txt.txt')
        #entities_json_data = json.loads(Entityobject['Body'].read())
        #originalData = originalDataObject['Body'].read().decode()
        
        originalData = event['data']
        entities_json_data = event['entities']
        # Mask entities
        deidentified_message, entity_map = deidentify_entities_in_message(originalData, entities_json_data)
        hashed_message = store_deidentified_message(deidentified_message, entity_map, 'LookUp')
        return deidentified_message
    except Exception as e:
      logging.error('Exception: %s. Unable to extract entities from message' % e)
      raise e