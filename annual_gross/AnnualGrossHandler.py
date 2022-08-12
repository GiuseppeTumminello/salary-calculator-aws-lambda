import json
import AnnualGrossCalculation
import DynamoDb
import Sqs
import ast
DESCRIPTION = 'Annual gross'


def annual_gross_handler(event, context):
    message = ast.literal_eval(str(Sqs.read_message_from_queue()))
    annual_gross = AnnualGrossCalculation.calculate_annual_gross(message['amount'])
    Sqs.send_message_to_queue(json.dumps({DESCRIPTION: annual_gross, 'uuid': message['uuid']}))
    DynamoDb.save_data(annual_gross)
    return json.dumps({DESCRIPTION: annual_gross})


