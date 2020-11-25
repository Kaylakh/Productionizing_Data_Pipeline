import requests
import urllib.request
from bs4 import BeautifulSoup
import boto3
import json
from urllib.parse import unquote_plus

s3_client = boto3.client('s3')


def lambda_handler(event,context):
    try:
        url = event['url']
        print(url)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

        #url ='https://seekingalpha.com/article/4391086-diana-shipping-inc-dsx-ceo-simeon-palios-on-q3-2020-results-earnings-call-transcript'
        response = requests.get(url, headers=headers,  proxies={'http':'138.68.60.8	:8080'})
        print(response)
        soup= BeautifulSoup(response.text,"html.parser")
        content = soup.find('div', class_ = "sa-art article-width")

        article = ''
        for i in content.findAll('p'):
            article = article + ' ' + i.text
        print("Scraping completed")
        print( article)

        # put the bucket name you create in step 1
        bucket_name = "assign2-scrape-bucket"
        file_name = "test.txt"
        s3_path = "ScrapedFolder/" + file_name
        s3 = boto3.resource("s3")

        #upload_byte_stream = bytes(json.dumps(article).encode('UTF-8'))
        s3.Bucket(bucket_name).put_object(Key=s3_path, Body=article)
        response = { 's3_path where file stored': s3_path,'Scraped data': article}
        return response

    except Exception as e:
        print(e)


