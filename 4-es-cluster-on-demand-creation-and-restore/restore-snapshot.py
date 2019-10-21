import boto3
import requests
from requests_aws4auth import AWS4Auth

host = 'https://vpc-elastic-search-domain-olp-kr3zgrug73z73lst4c675du3uq.eu-central-1.es.amazonaws.com/' # include https:// and trailing /
region = 'eu-central-1' # e.g. us-west-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

path = '_snapshot/logs-xyz-index-snapshot-repo/*/_restore'
url = host + path

payload = {
  "indices": "logs-xy*"
}

headers = {"Content-Type": "application/json"}

r = requests.post(url, auth=awsauth, json=payload, headers=headers)

print(r.status_code)
print(r.text)