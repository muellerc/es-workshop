import json
import os
from elasticsearch import Elasticsearch

ES_DOMAIN_ENDPOINT = os.environ['ES_DOMAIN_ENDPOINT']

es = Elasticsearch()

def lambda_handler(event, context):
    print('received event: {}'.format(json.dumps(event)))
    es.

    return