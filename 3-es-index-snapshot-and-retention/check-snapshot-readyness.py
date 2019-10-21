import boto3
import json
import requests
from requests_aws4auth import AWS4Auth

host = 'https://vpc-elastic-search-domain-olp-kr3zgrug73z73lst4c675du3uq.eu-central-1.es.amazonaws.com/' # include https:// and trailing /
region = 'eu-central-1' # e.g. us-west-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

path = '_snapshot/logs-xyz-index-snapshot-repo/_status'
url = host + path

r = requests.get(url, auth=awsauth)

print(r.status_code)
print(r.text)

response = json.loads(r.text)
if not response.get('snapshots'):
  print("response is empty")
