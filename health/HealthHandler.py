import json
import HealthCalculator
import DynamoDb
import Sqs
import ast
DESCRIPTION = 'Health'


def health_handler(event, context):
    message = ast.literal_eval(str(Sqs.read_message_from_queue()))
    health = HealthCalculator.calculate_health(message['amount'])
    Sqs.send_message_to_queue(json.dumps({DESCRIPTION: health, 'uuid': message['uuid']}))
    DynamoDb.save_data(health)
    return json.dumps({DESCRIPTION: health})
