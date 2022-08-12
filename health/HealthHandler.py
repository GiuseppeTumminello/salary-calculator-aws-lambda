import json
import HealthCalculator
import DynamoDb
import Sqs
import ast
DESCRIPTION = 'Health'


def health_handler(event, context):
    message = Sqs.read_message_from_queue()
    monthly_gross = ast.literal_eval(str(message))
    print(monthly_gross)
    health = HealthCalculator.calculate_health(monthly_gross['amount'])
    print(health)
    Sqs.send_message_to_queue(json.dumps({DESCRIPTION: monthly_gross['amount'], 'uuid': monthly_gross['uuid']}))
    DynamoDb.save_data(health)
    return json.dumps({DESCRIPTION: health})
