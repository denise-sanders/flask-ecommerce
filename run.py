#!flask/bin/python
from app import app
from pathlib import Path
import os.path

import sys

port = 5000

try:
    cert_file = app.config['CERT_FILE']
    key_file = app.config['KEY_FILE']

    if not os.path.isfile(cert_file):
        raise FileNotFoundError
    if not os.path.isfile(key_file):
        raise FileNotFoundError

    context = (cert_file, key_file)
    app.run(host='0.0.0.0', port=port, ssl_context=context, threaded=True, debug=True)

except FileNotFoundError as e:
    try:
        print("SSL Failed, could not find cert of key file.\nStarting server without ssl") #TODO: remove this in prod
        app.run(host='0.0.0.0', port=port, threaded=True, debug=True)
    except:
        print("Starting server without ssl failed")
        exit(1)
except Exception as e:
    print("Unknown error {0}".format(type(e).__name__))
