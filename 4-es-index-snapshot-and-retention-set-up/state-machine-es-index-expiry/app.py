import json
import os
from elasticsearch import Elasticsearch

ES_DOMAIN_ENDPOINT = os.environ['ES_DOMAIN_ENDPOINT']

es = Elasticsearch(
    [ES_DOMAIN_ENDPOINT + ':443'],
    use_ssl=True,
    verify_certs=True,
)

def lambda_handler(event, context):
    print('received event: {}'.format(json.dumps(event)))

    # ignore 404 and 400
    es.indices.delete(index='test-index', ignore=[400, 404])

    return