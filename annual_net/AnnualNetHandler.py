import json
import AnnualNetCalculation
import DynamoDb
import Sqs
import ast
DESCRIPTION = 'Annual net'


def annual_net_handler(event, context):
    message = ast.literal_eval(str(Sqs.read_message_from_queue()))
    annual_net = AnnualNetCalculation.calculate_annual_net(message['amount'])
    Sqs.send_message_to_queue(json.dumps({DESCRIPTION: annual_net, 'uuid': message['uuid']}))
    DynamoDb.save_data(annual_net)
    return json.dumps({DESCRIPTION: annual_net})
