
import json
import boto3
import logging
import threading
import sys

s3 = boto3.client('s3')

def mask_entities_in_message(message, entity_list):
  for entity in entity_list:
      message = message.replace(entity['Text'], '#' * len(entity['Text']))
  return message

def lambda_handler(event, context):
  try:
      #originalDataObject= s3.get_object(Bucket = 'assign2-scrape-bucket', Key= 'ScrapedFolder/webscrape.txt')
      #Entityobject= s3.get_object(Bucket = 'assign2-scrape-bucket', Key= 'EntityExtractionOutput/webscrape.txt.txt')
      #entities_json_data = json.loads(Entityobject['Body'].read())
      #originalData = originalDataObject['Body'].read().decode()
      
      originalData = event['data']
      entities_json_data = event['entities']
      print(originalData, entities_json_data)
      
      masked_data = mask_entities_in_message(originalData, entities_json_data)
      return masked_data
     
  except Exception as e:
      logging.error('Exception: %s. Unable to get the data from s3' % e)
      raise e