import json
from textblob import TextBlob

def lambda_handler(event, context):
    try:
        text = event['text']
        blob = TextBlob(text)
        sentiment = "positive" if blob.sentiment.polarity > 0 else "negative" if blob.sentiment.polarity < 0 else "neutral"
        return {
            'statusCode': 200,
            'body': json.dumps({'sentiment': sentiment})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
