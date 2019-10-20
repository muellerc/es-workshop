+++
title = "Bootstrap AWS Cloud9"
draft = true
weight = 11
pre = "1.1 "
+++

{{% notice tip %}}
Ad blockers, javascript disablers, and tracking blockers should be disabled for
the cloud9 domain, or connecting to the workspace might be impacted.
Cloud9 requires third-party-cookies. You can whitelist the [specific domains]( https://docs.aws.amazon.com/cloud9/latest/user-guide/troubleshooting.html#troubleshooting-env-loading).
{{% /notice %}}

{{% notice info %}}
You have to chose whether you want to provision your Cloud9 IDE in an existing VPC and subnet, or whether you want to create a new, dedicated VPC with two subnets for this workshop. Please refer to the coresponding section, depending your choice.
{{% /notice %}}

### 1. Create the Cloud9 IDE

{{< tabs name="Region" >}}
{{< tab name="Oregon" include="us-west-2" />}}
{{< tab name="Ireland" include="eu-west-1" />}}
{{< tab name="Ohio" include="us-east-2" />}}
{{< tab name="Singapore" include="ap-southeast-1" />}}
{{< /tabs >}}


### 2. Launch the AWS CloudFormation stack

Review the **Parameter** and click **Create Stack** at the bottom of the page to launch the stack.


### 3. Wait until the AWS CloudFormation stack launched

It takes usualy less than 2 minutes until the stack launched. When the stack is launched, the status will change from **CREATE_IN_PROGRESS** to **CREATE_COMPLETE**.

{{%expand "Screenshot" %}}
![Step 1](/images/prerequisits/image-1.png)
{{% /expand%}}


## 4. Open your AWS Cloud9 IDE

The **Outputs** tab in your CloudFormation console exposes the **Cloud9DevEnvUrl** parameter. Click at the coresponding URL in the value column and open your AWS Cloud9 development environment in a new tab.

{{%expand "Screenshot" %}}
![Step 2](/images/prerequisits/image-2.png)
{{% /expand%}}
