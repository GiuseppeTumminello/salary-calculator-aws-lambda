import json
import DynamoDb, Sns
import Sqs


def salary_calculator_handler(event, context):
    messages_from_queue = json.loads(json.dumps((Sqs.read_message_from_queue(event))))
    microservice_data = []
    print(messages_from_queue)
    for description, value in messages_from_queue.items():
        microservice_data.append(description)
        microservice_data.append(value)

    DynamoDb.save_data(microservice_data[1], microservice_data[3], microservice_data[0])
    return messages_from_queue
