# Amazon-Review-Analysis
Simple Amazon Bedrock demo showing how to extract key elements from Amazon Reviews

## Disclamer
This code is designed for demonstration purposes and may not adhere to standard best practices.
Authored by Maxence Pastor, this code is a personal project and not owned by Amazon Web Services.
Neither Amazon nor I hold liability for any issues arising from this code.
Please note, executing this code may incur costs on your account.

## Goal

The goal is simple: demonstrate how to make a simple Amazon review parser / analyser using Amazon Bedrock. 

Here is an example: 

![Screenshot](https://github.com/maxpastor/Amazon-Review-Analysis/blob/main/resources/Screenshot.png)

## How to use 

- 1: Create a small Cloud9 instance on your AWS account
- 2: Ask for access to Amazon Bedrock models in your region (approval is instant)
- 3: Create a role for your Cloud9 instance with the right permissions (Amazon Bedrock), don't forget to follow the principle of least privilege
- 4: Assign the role to the instance in the EC2 console (top right-> actions -> security -> Modify IAM role)
- 5: In Cloud9, remove the AWS managed credentials (top right -> gear icon -> AWS Settings -> Credentials -> Turn Off)
- 6: Run the following commands
- 7: Click on "Preview > Preview Running Application" in of the Cloud9 top menu bar
- 8: Paste a review and enjoy!

### You might want to change the region in the code as it is US-WEST-2 at the moment
```bash
# if you do not have >= python 3.9 installed, please upgrade like described here:
# https://tecadmin.net/install-python-3-9-on-amazon-linux/
# Clone the repository
git clone https://github.com/typex1/Amazon-Review-Analysis.git
cd Amazon-Review-Analysis
pip install -r requirements.txt
streamlit run app.py --server.port 8080
```

## How it works: 

We get the review string, pass it to Amazon Bedrock and parse the XML output with a regex in order to extract the elements.

The prompt is specifically asking for Claude to output the response in XML (which it is very good at doing), so that we can parse it easily.

### And voila!

Tweak things, play with the prompt and the temperature, and see how it goes 🤗 ! 




