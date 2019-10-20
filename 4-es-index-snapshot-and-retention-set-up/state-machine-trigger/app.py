import json
import os
import datetime

STATE_MACHINE_ARN = os.environ['STATE_MACHINE_ARN']

config = Config(connect_timeout=5, read_timeout=5, retries={'max_attempts': 5})
stepfunctions = boto3.client('stepfunctions', config=config)

def lambda_handler(event, context):
    print('received event: {}'.format(json.dumps(event)))
    now = datetime.datetime.utcnow().isoformat()

    response = stepfunctions.start_execution(
        stateMachineArn = STATE_MACHINE_ARN,
        name = now,
        input = '{}'
    )

    return