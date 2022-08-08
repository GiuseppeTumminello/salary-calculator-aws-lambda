import boto3

sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-east-1.amazonaws.com/342003767516/salary-calculator-orchestrator-queue'


class Sqs:
    def send_message_to_queue(self):
        sqs.send_message(QueueUrl=queue_url, MessageAttributes={'amount': self, })
