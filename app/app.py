import json
from transformers import pipeline

# Load classifier on lambda start-up. 
# Like this we share the classifier over different instances of our lambda function.
classifier = pipeline('sentiment-analysis', model="./model/", tokenizer="./model/")

def handler(event, context):
    # we expect a "data" key in the "body" of our event.
    data = json.loads(event["body"])["data"]
    print(f"making a prediction on the text: {data}")
    # make prediction
    prediction = classifier(data)
    print(f"prediction: {prediction}")
    return {
        'statusCode': 200,
        'body': json.dumps(prediction)
    }