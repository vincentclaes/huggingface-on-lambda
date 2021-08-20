# huggingface-on-lambda

- follow the steps in the notebook [huggingface_pretrained_model.ipynb](./huggingface_pretrained_model.ipynb)
- open an AWS cloudshell

      git clone https://github.com/vincentclaes/huggingface-on-lambda.git
      npm install --prefix ./ serverless
      node_modules/serverless/bin/serverless.js deploy
      curl -X POST https://8af9ar02gi.execute-api.eu-west-1.amazonaws.com/dev/prediction
