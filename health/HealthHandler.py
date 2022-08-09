import json

import HealthCalculator
import DynamoDb
import Sqs

DESCRIPTION = 'Health'


def health_handler(event, context):
    message = json.loads(Sqs.read_message_from_queue())
    monthly_gross = message['amount']
    health = HealthCalculator.calculate_health(monthly_gross)
    Sqs.send_message_to_queue(json.dumps({DESCRIPTION: health}))
    DynamoDb.save_data(health)
    return json.dumps({DESCRIPTION: health})
