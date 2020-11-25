# Productionizing_Data_Pipeline

1. Scrapes data from earning call transcripts (See https://seekingalpha.com/earnings/earnings-call-transcripts (Links to an external site.)) and stores them in S3
2. Anonmyizes the data through:
·       Masking
·       Anonymization
  With ability to deanonymize
  No deanonymization possibility
3. Deanonymize for fields that can be deanonymized
Then, building upon the Infrastructure for login and server less functions using Cognito , integrate the APIs so that
1. Only authenticated users can call these APIs
2. Use Amazon Step functions and Lamda functions to make it server less 

