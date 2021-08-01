from logging import INFO
from typing import Dict
from flask import Flask, request
from flask.logging import create_logger
from dialogflow_fulfillment import WebhookClient

# Create Flask app and enable info level logging
app = Flask(__name__)
logger = create_logger(app)
logger.setLevel(INFO)


def handler(agent: WebhookClient) -> None:
    """Handle the webhook request.."""
    print("agent..........",agent)


@app.route('/webhook', methods=['POST'])
def webhook() -> Dict:
    """Handle webhook requests from Dialogflow."""
    # Get WebhookRequest object
    request_ = request.get_json(force=True)
    param_keys = request_["queryResult"]["parameters"].keys()
    for param_value in param_keys:
        print("value::::::::::::::::", param_value)

    # Log request headers and body
    logger.info(f'Request headers: {dict(request.headers)}')
    print("--------------------------------------------------")
    logger.info(f'Request body: {request_}')

    # Handle request
    agent = WebhookClient(request_)
    agent.handle_request(handler)

    # Log WebhookResponse object
    print("---------------------------------------------------------")
    logger.info(f'Response body: {agent.response}')

    # return agent.response
    return {'fulfillment_text': "from sri laptop"}


if __name__ == '__main__':
    app.run(debug=True)