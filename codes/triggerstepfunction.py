import json
import boto3
import time
import uuid 
  

client = boto3.client('stepfunctions')

def lambda_handler(event, context):
   
    floc = event['filelocation']
    fdic = event['decision'] 
    id = uuid.uuid1()
    
    response = client.start_execution(
      input= "{\"key\": \"%s\", \"decision\": \"%s\"}" %(floc,fdic),
      name =str(id),
      stateMachineArn= "arn:aws:states:us-east-1:284378271947:stateMachine:DataPipeline"
)
    execArn = response['executionArn']
    
    time.sleep(15)
    result = client.describe_execution(executionArn= execArn)
    output = result['output']
    return output
    
