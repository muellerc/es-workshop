+++
title = "Amazon Elasticsearch Service index snapshot and retention"
draft = true
weight = 30
pre = "3. "
+++

```bash
aws iam create-policy 
  --policy-name ElasticsearchCuratorIndexSnapshotPolicy \
  --policy-document file://policy.json
```

```yaml
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "s3:ListBucket"
      ],
      "Effect": "Allow",
      "Resource": [
        "arn:aws:s3:::<<REPLACE_WITH_S3_BUCKET_NAME>>"
      ]
    },
    {
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject"
      ],
      "Effect": "Allow",
      "Resource": [
        "arn:aws:s3:::<<REPLACE_WITH_S3_BUCKET_NAME>>/*"
      ]
    }
  ]
}
```

```bash

```
aws iam create-role \
  --role-name ElasticsearchCuratorIndexSnapshotRole \
  --assume-role-policy-document file://role-policy.json
```

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "es.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

```bash
export POLICY_ARN=$(aws iam list-policies --query 'Policies[?PolicyName==`ElasticsearchCuratorIndexSnapshotPolicy`].[Arn]' --output=text)

echo "POLICY_ARN=${POLICY_ARN}"

aws iam attach-role-policy \
  --role-name ElasticsearchCuratorIndexSnapshotRole \
  --policy-arn ${POLICY_ARN}

```


```bash
aws iam list-roles --query 'Roles[?RoleName==`ElasticsearchCuratorIndexSnapshotRole`].[Arn]' --output=text
```

```
PUT _snapshot/logs-xyz-index-snapshot-repo
{
  "type": "s3",
  "settings": {
    "bucket": "cmr-logs-xyz-index-snapshot-repo",
    "region": "eu-central-1",
    "role_arn": "arn:aws:iam::689573718314:role/ElasticsearchCuratorIndexSnapshotRole"
  }
}
```

pip3 install -r requirements.txt

python3 register-snapshot-repo.py


PUT _snapshot/logs-xyz-index-snapshot-repo
{
  "type": "s3",
  "settings": {
    "bucket": "logs-xyz-index-snapshot-repo",
    "region": "eu-central-1",
    "role_arn": "arn:aws:iam::689573718314:role/ElasticsearchCuratorIndexSnapshotRole"
  }
}

GET _snapshot/



503
{"error":{"root_cause":[{"type":"concurrent_snapshot_execution_exception","reason":"[logs-xyz-index-snapshot-repo:2019-10-18-15-x]  a snapshot is already running"}],"type":"concurrent_snapshot_execution_exception","reason":"[logs-xyz-index-snapshot-repo:2019-10-18-15-x]  a snapshot is already running"},"status":503}