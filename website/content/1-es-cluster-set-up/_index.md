+++
title = "Amazon Elasticsearch Service cluster set-up"
draft = false
weight = 10
pre = "1. "
+++

Not surprisingly, we will kick of the workshop with provisioning our **[Amazon Elasticsearch Service](https://aws.amazon.com/elasticsearch-service/)** cluster. The easiest, fastest and a repeatable way of doing it, is of course using **[AWS CloudFormation](https://aws.amazon.com/cloudformation/)**. We provide you with an AWS CloudFormation template which allows you to provision the Amazon Elasticsearch Service cluster in a new VPC within your account. If you cannot create a new VPC for whatever reason, chose the AWS CloudFormation template which will deploy the Amazon Elasticsearch Service cluster into an existing VPC.

{{% notice note %}}
We recommend running this workshop in the mode where we are creating a **new VPC**, instead of reusing an existing one. In this way we can make sure that all the connectivity and firewalls are set up correctly.
{{% /notice %}}

{{% notice info %}}
If you run this workshop in your own AWS account, you should calculate with **~ $ 18 per day** in AWS spend in the default set-up (3 m5.large master nodes, 2 m5.large data notes). After you finished the workshop, make sure you are running the **clean-up** lab to de-provision all resources, so that no addition cost occurs.
{{% /notice %}}

| AWS CloudFormation launch template | Launch in a new VPC | Launch in an existing VPC |
| ------ |:------:|:--------:|
| Amazon Elasticsearch Service cluster | {{% cf-launch "ee-assets-prod-us-east-1/modules/feb8f3a5c330462185636c0af0e4a536/v1/es-cluster-set-up-template-new-vpc.yaml" "es-workshop-lab-1" %}} | {{% cf-launch "ee-assets-prod-us-east-1/modules/feb8f3a5c330462185636c0af0e4a536/v1/es-cluster-set-up-template-existing-vpc.yaml" "es-workshop-lab-1" %}} |  

{{%expand "Details" %}}


![Image 1](/images/1-es-cluster-set-up/index-1.png)
{{% /expand%}}

This deployment will **take roughly 15 minutes**, depending whether we have to create a new VPC, subnets, internet gateways, route tables or not, and the number of nodes and instance types we will provision. Now it's a good time to **get a Coffee**, lean back and have a look at the AWS CloudFormation template we are deploying.  

{{% notice tip %}}
If you don't understand all the pieces in the AWS CloudFormation template, just raise your hand and we are happy to explain it to you. In this way, you can **maximize the learnings for you**!
{{% /notice %}}

| AWS CloudFormation template | Launch in a new VPC | Launch in an existing VPC |
| ------ |:------:|:--------:|
| Amazon Elasticsearch Service cluster | {{% cf-download "ee-assets-prod-us-east-1/modules/feb8f3a5c330462185636c0af0e4a536/v1/es-cluster-set-up-template-new-vpc.yaml" %}} | {{% cf-download "ee-assets-prod-us-east-1/modules/feb8f3a5c330462185636c0af0e4a536/v1/es-cluster-set-up-template-existing-vpc.yaml" %}} | 
