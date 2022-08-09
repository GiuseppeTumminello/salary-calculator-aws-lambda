import json
import DynamoDb
import Sqs
import TaxCalculator

DESCRIPTION = 'Tax'


def tax_handler(event, context):
    message = json.loads(Sqs.read_message_from_queue())
    monthly_gross = message['amount']
    tax = TaxCalculator.calculate_health(monthly_gross)
    Sqs.send_message_to_queue(json.dumps({DESCRIPTION: tax}))
    DynamoDb.save_data(tax)
    return json.dumps({DESCRIPTION: tax})
