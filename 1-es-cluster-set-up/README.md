# Setup process

Firstly, we need an `Amazon S3 bucket` where we can upload our artifacts (SAM/CloudFormation template) packaged as ZIP before we deploy anything - If you don't have a S3 bucket to store code artifacts then this is a good time to create one:

```bash
aws s3 mb s3://<BUCKET_NAME>
```

Next, run the following command to package our SAM template to Amazon S3:

```bash
sam package \
    --template-file template.yaml \
    --output-template-file packaged.yaml \
    --s3-bucket <BUCKET_NAME>
```

Next, the following command will create a Cloudformation Stack and deploy your SAM resources:

```bash
sam deploy \
    --template-file packaged.yaml \
    --stack-name amazon-es-workshop-lab-1
```

If you want to override some of the default parameters, run the following adapted command instead:

```bash
sam deploy \
    --template-file packaged.yaml \
    --stack-name amazon-es-workshop-lab-1 \
    --parameter-overrides "ParameterKey1=ParameterValue1 ParameterKey2=ParameterValue2"
```

After deployment is complete you can run the following command to retrieve the Amazon ElasticSearch Service domain endpoint:

```bash
aws cloudformation describe-stacks \
    --stack-name ElasticSearchCluster \
    --query 'Stacks[].Outputs[?OutputKey==`DomainEndpoint`]' \
    --output table
``` 

## ElasticSearch commands

### Creating Snapshots Repository

curl -XPUT 'elasticsearch-domain-endpoint/_snapshot/repository-name'

```
curl -XPUT 'https://es-domain/_snapshot/my-snapshot-repo?verify=false&pretty' -d'
{
  "type": "s3",
  "settings": {
    "bucket": "elasticsearch-backup-indices",
    "region": "us-west-2",
    "role_arn": "arn:aws:iam::YOUR-ACCOUNT-ID:role/es-s3-backup"
  }
}'
```


### Test Elasticsearch & Kibana access

curl -k -XGET "https://localhost:9200/_search" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match_all": {}
  }
}' | jq '.'





### Taking Manual Snapshots

#### All Indexes

```
curl -XPUT 'https://es-domain/_snapshot/snapshot-repo-name/2019-01-19?pretty&wait_for_completion=true'
```

#### Single Indexe

```
curl -XPUT 'https://es-domain/_snapshot/my-snapshot-repo/2019-01–19?pretty&wait_for_completion=true' -d'
{
 “indices”: “alb-accesslog-2018–08–28”,
 “ignore_unavailable”: true,
 “include_global_state”: false
}'
```

### Verify Snapshots State

```
curl -XGET ‘https://es-domain/_snapshot/my-snapshot-repo/_all?pretty'
```

```
curl -XGET 'http://es-domain/_cat/snapshots/s3_repository?v'
```

### Restoring Single Index

```
curl -XPOST 'es-domain/_snapshot/my-snapshot-repo/2019-01–19/_restore' -H 'Content-Type: application/json' -d'
{
  "indices": "index_1,index_2",
  "ignore_unavailable": false,
  "include_global_state": false
}'
```

### Restoring All Indexes

```
curl -XPOST 'es-domain/_snapshot/my-snapshot-repo/2019-01–19/_restore'
```

### Delete A Single Index

```
curl -XDELETE 'es-domain/index-name'
```

### Delete All Indexes

```
curl -XDELETE 'https://es-domain/_all'
```


## Useful resources
https://medium.com/docsapp-product-and-technology/aws-elasticsearch-manual-snapshot-and-restore-on-aws-s3-7e9783cdaecb