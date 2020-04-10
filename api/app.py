"""
Main API entry point.

This file also contains the definition of the flask application that handles Http requests.
"""

# System imports
import logging

# Third-party imports
from flask import Flask, json, jsonify, request, make_response
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
import numpy as np

LOGGER = logging.getLogger(__name__)

app = Flask(__name__)
api = Api(app)
CORS(app)


@app.route("/health")
def health():
    """
    Expose an endpoint that can be used to check the health of the API.
    """
    return jsonify({
        "status": {
            "code": 200,
            "status": "SUCCESS!"
        }
    })


class AddProduct(Resource):
    """
    Add a grocery product to inventory.
    """
    @staticmethod
    def post():

        parse = reqparse.RequestParser()
        parse.add_argument('product')

        np.random.seed(5)
        samples = np.asarray(request.get_json()['product'])

        return make_response(jsonify({'product': samples.tolist()}))


api.add_resource(AddProduct, '/add_product')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=3500)
