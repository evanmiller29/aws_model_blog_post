Hosting a ML model on AWS Lambdas + API Gateway
So you've toiled forweeks (months cough cough)and you're beautiful machine learning model is done. Thank god.
But now someone wants to use your model. That's great news ain't it? 
It definitely is, but a whole new problem comes up. You've gotta put it some where and make it available to other people in the business. 
This tutorial will show you how to use AWS to do this. In specific we'll be using the following components:
API gateway
S3 buckets
Lambda functions/lambda layers

I'm not using Sagemaker because it can be quite expensive £100 p/m per model opposed to lambda functions where you just pay per request.
You'll need a few things to complete this. You'll need an installation of Python (scikit learn, pandas etc) and Docker installed. 
Docker will be needed to build the correct lambda layer files if you are on a Windows machine (I learned this the hard way)