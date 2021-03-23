# -*- coding: utf-8 -*-

from flask import Flask, make_response, request, abort

import json
import os

SHARED_KEY = os.environ.get('ONVA_SHARED_KEY')

assert SHARED_KEY, 'Must specify ONVA_SHARED_KEY in the environment'

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('Content-Type') != 'application/json':
        abort(400)

    if 'X-Onva-Shared-Key' not in request.headers:
        abort(400)

    if request.headers['X-Onva-Shared-Key'] != SHARED_KEY:
        abort(400)

    payload = request.json

    # payload contains:
    #   event_type - can be ping, submission.created, submission.answer, or submission.complete
    #   event_uuid - a unique identifier for the event
    #   retry_number - how many times delivery of this event has been tried before this event
    #   data - this will contain a different object depending on the event_type
    #       ping - will be an empty object
    #       submission.complete will be a submission object, see https://api.onva.io/redoc/#operation/submission_get
    event_type = payload['event_type']

    if event_type == 'ping':
        pass

    elif event_type == 'submission.complete':
        print(json.dumps(payload, indent=4))

        # this would represent the identifier used for the user
        # identifier = payload['data']['identifier']

    return make_response('', 200)
