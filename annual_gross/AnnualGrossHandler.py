
import json
from annual_gross.AnnualGrossCalculation import AnnualGross
from annual_gross.DynamoDb import DynamoDb
from annual_gross.Sqs import Sqs

DESCRIPTION = 'Annual gross'


def annual_gross_handler(event):
    message = json.loads(Sqs.read_message_from_queue())
    monthly_gross = message['amount']
    annual_gross = AnnualGross.calculate_annual_gross(monthly_gross)
    Sqs.send_message_to_queue(annual_gross)
    DynamoDb.save_data(annual_gross)
    print(message)
    return {DESCRIPTION: annual_gross}





annual_gross_handler(6000)

