# Huggingface on Lambda

Follow the steps in the (sagemaker) notebook [huggingface_pretrained_model.ipynb](./huggingface_pretrained_model.ipynb).

Here we will:

 - read a model from huggingface
 - save it locally
 - create a docker file, build and push to ecr
 - create a serverless file that points to our docker image
 - deploy our model behind a lambda function and connect with an api gateway
 - provision at least 1 hot lambda to get sub second responses!
 - call our model using curl
