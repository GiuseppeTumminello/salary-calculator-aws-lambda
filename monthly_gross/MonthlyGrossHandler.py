import json
import DynamoDb
import Sqs

DESCRIPTION = 'Monthly gross'


def monthly_gross_handler(event, context):
    message = json.loads(Sqs.read_message_from_queue())
    monthly_gross = message['amount']
    uuid = message['uuid']
    Sqs.send_message_to_queue(json.dumps({DESCRIPTION: monthly_gross}))
    DynamoDb.save_data(monthly_gross, uuid)
    return json.dumps({DESCRIPTION: monthly_gross})
