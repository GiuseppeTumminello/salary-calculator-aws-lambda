import json

import DisabilityZusCalculator
from DynamoDb import DynamoDb
import Sqs

DESCRIPTION = 'Disability zus'


def disability_zus_handler(event, context):
    message = json.loads(Sqs.read_message_from_queue())
    monthly_gross = message['amount']
    disability_zus = DisabilityZusCalculator.calculate_disability_zus(monthly_gross)
    Sqs.send_message_to_queue(json.dumps({DESCRIPTION: disability_zus}))
    DynamoDb.save_data(disability_zus)
    return json.dumps({DESCRIPTION: disability_zus})
