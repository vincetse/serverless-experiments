#!/usr/bin/env python
from flask import Flask
from flask import jsonify
from flask import request
import uuid

app = Flask("id-service")

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/uuid")
def get_uuid():
    n = request.args.get("n")
    if n is None:
        n = 1
    uuids = []
    for i in xrange(int(n)):
        uuids.append(uuid.uuid4())
    body = {
        "uuid": uuids
    }
    return jsonify(body)

if __name__ == "__main__":
    app.run()
