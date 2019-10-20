+++
title = "Configure AWS Cloud9"
draft = true
weight = 12
pre = "1.2 "
+++


### 1. Configure your AWS Cloud9 development environment

In your AWS Cloud9 IDE, you can close the welcome tab. In the left environment navigation window, you can see the project **wild-rydes-async-messaging** we have already checked out for you from Github. This project also contains a shell script to setup your environment. Run the following command in the **bash** tab (at the bottom of the IDE):

{{%expand "Screenshot" %}}
![Step 3](/images/prerequisits/image-3.png)
{{% /expand%}}

{{< highlight bash >}}
cd wild-rydes-async-messaging/lab-0 && \
chmod +x configureCloud9.sh && \
./configureCloud9.sh
{{< /highlight >}}

{{%expand "Screenshot" %}}
![Step 4](/images/lab-0-step-4.png)
{{% /expand%}}

![Get Started](/images/magic.gif)

**You are now ready to get started!!!**
