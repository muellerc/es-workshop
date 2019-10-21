import boto3
from datetime import datetime, timedelta
import requests
from requests_aws4auth import AWS4Auth

host = 'https://vpc-elastic-search-domain-olp-kr3zgrug73z73lst4c675du3uq.eu-central-1.es.amazonaws.com/' # include https:// and trailing /
region = 'eu-central-1' # e.g. us-west-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)


last_hours = datetime.now() + timedelta(hours=-1)
path = 'logs-xyy-' + last_hours.strftime("%Y-%m-%d-%H") 
url = host + path

payload = {
  "index": {
    "blocks.read_only": "true"
  }
}

headers = {"Content-Type": "application/json"}

r = requests.put(url, auth=awsauth, json=payload, headers=headers)

# we can omit the payload and header, if we want to snapshot the entire cluster
r = requests.put(url, auth=awsauth)

print(r.status_code)
print(r.text)



# # Restore snapshots (all indices)
#
# path = '_snapshot/my-snapshot-repo/my-snapshot/_restore'
# url = host + path
#
# r = requests.post(url, auth=awsauth)
#
# print(r.text)
#
# # Restore snapshot (one index)
#
# path = '_snapshot/my-snapshot-repo/my-snapshot/_restore'
# url = host + path
#
# payload = {"indices": "my-index"}
#
# headers = {"Content-Type": "application/json"}
#
# r = requests.post(url, auth=awsauth, json=payload, headers=headers)
#
# print(r.text)