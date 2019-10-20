+++
title = "Configure AWS Cloud9"
draft = true
weight = 12
pre = "1.2 "
+++

https://aws.amazon.com/blogs/database/set-access-control-for-amazon-elasticsearch-service/

https://aws.amazon.com/premiumsupport/knowledge-center/kibana-outside-vpc-ssh-elasticsearch/



ssh -i ~/.ssh/your-key.pem ec2-user@your-ec2-instance-public-ip -N -L 9200:vpc-your-amazon-es-domain.region.es.amazonaws.com:443


PUT _snapshot/logs-xyz-index-snapshot-repo
{
  "type": "s3",
  "settings": {
    "bucket": "logs-xyz-index-snapshot-repo",
    "region": "eu-central-1",
    "role_arn": "arn:aws:iam::689573718314:role/ElasticsearchCuratorIndexSnapshotRole"
  }
}

GET _snapshot/logs-xyz-index-snapshot-repo

GET _snapshot/logs-xyz-index-snapshot-repo/2019-10-18-15

GET _snapshot/_status

GET _snapshot/logs-xyz-index-snapshot-repo/_status

GET _snapshot/logs-xyz-index-snapshot-repo/_all?pretty

POST _snapshot/logs-xyz-index-snapshot-repo/_verify

GET logs-xyy-2019-10-18-16/_settings

GET logs-xyy-2019-10-18-16/_stats