import boto3
client = boto3.client('sns')


def lambda_handler(event, context):
  response = client.publish(TopicArn='arn:aws:sns:us-east-1:255945442255:Rger-Mailer',Message="default message")
  print("Message published AGAIN!")
  return(response)
