+++
title = "Provisioning Amazon Elasticsearch Service"
draft = true
weight = 31
pre = "3.1 "
+++


GET logs-xyy-2019-10-18-16/_stats


ssh -i /Users/cmr/esworkshop-eu-central-1.pem ec2-user@54.93.242.120 -N -L 9200:vpc-elastic-search-domain-olp-kr3zgrug73z73lst4c675du3uq.eu-central-1.es.amazonaws.com:443


GET /_cat/nodes?v

GET /_cat/indices?v

PUT /logs-xyy-2019-10-21

GET /logs-xyy-2019-10-21

PUT /logs-xyy-2019-10-21/_alias/logs-xyy

GET /logs-xyy

DELETE /logs-xyy-2019-10-21

PUT /logs-xyy-2019-10-21
{
  "aliases": {
    "logs-xyy": {}
  },
  "settings": {
    "number_of_shards": 2,
    "number_of_replicas": 1
  }
}

GET /logs-xyy-2019-10-21

GET /logs-xyy

GET /_cat/indices?v

PUT _template/logs-xyy
{
  "aliases": {
    "logs-xyy": {}
  },
  "settings": {
    "number_of_shards": 2,
    "number_of_replicas": 1
  },
  "index_patterns": ["logs-xyy-*"]
}

GET _template/logs-xyy

PUT /logs-xyy-2019-10-22

GET /logs-xyy-2019-10-22

GET /logs-xyy