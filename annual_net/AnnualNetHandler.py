import json
from DynamoDb import DynamoDb
from AnnualNetCalculation import AnnualNetCalculation
from Sqs import Sqs

DESCRIPTION = 'Annual net'


def annual_net_handler(event, context):
    message = json.loads(Sqs.read_message_from_queue())
    monthly_gross = message['amount']
    annual_net = AnnualNetCalculation.calculate_total_zus(monthly_gross)
    send_message = json.dumps({DESCRIPTION: annual_net})
    Sqs.send_message_to_queue(send_message)
    DynamoDb.save_data(annual_net)
    return json.dumps({DESCRIPTION: annual_net})
