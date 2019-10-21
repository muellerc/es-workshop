+++
title = "AWS Cloud9 set-up"
draft = true
weight = 20
pre = "2. "
+++

We will use **[AWS Cloud9](https://aws.amazon.com/cloud9/)** as our IDE in this workshop.

To run the workshop on your own, first we will provision an **[AWS Cloud9 IDE](https://aws.amazon.com/cloud9/)**. We will use this development environment during the workshop, because it has a couple advantages:  

+ we can make sure all dependencies are set up properly (AWS CLI, SAM CLI, Unix utilities, etc.)
+ we can directly access resources in your VPC
+ we can use the underlying **[Amazon EC2](https://aws.amazon.com/ec2/)** instance to create a local port forwarding tunnel to access the VPC resources via the internet from your locale machine  

| AWS CloudFormation launch template | Launch in an existing VPC |
| ------ |:------:|
| AWS Cloud9 IDE | {{% cf-launch "ee-assets-prod-us-east-1/modules/feb8f3a5c330462185636c0af0e4a536/v1/cloud9-set-up-template-existing-vpc.yaml" "es-workshop-lab-2" %}} |  

{{%expand "Details" %}}


![Image 1](/images/2-cloud9-set-up/index-1.png)
{{% /expand%}}

{{%expand "Details" %}}


![Image 2](/images/2-cloud9-set-up/index-2.png)
{{% /expand%}}

This deployment will **take roughly 1 - 2 minutes**. Have a look at the AWS CloudFormation template we are deploying, to learn more how to provision an AWS Cloud9 IDE.  

{{% notice tip %}}
If you don't understand all the pieces in the AWS CloudFormation template, just raise your hand and we are happy to explain it to you. In this way, you can **maximize the learnings for you**!
{{% /notice %}}

| AWS CloudFormation launch template | Launch in an existing VPC |
| ------ |:------:|
| AWS Cloud9 IDE | {{% cf-download "ee-assets-prod-us-east-1/modules/feb8f3a5c330462185636c0af0e4a536/v1/cloud9-set-up-template-existing-vpc.yaml" "es-workshop-lab-2" %}} |  
