"""
Main API entry point.

This file also contains the definition of the flask application that handles Http requests.
"""

# System imports
import logging

# Third-party imports
from flask import Flask, json, jsonify, request, make_response
from lxml.html import fromstring
from requests import get
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
import numpy as np
import time
import datetime

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
        parse.add_argument('barcode')

        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

        np.random.seed(5)
        barcode = np.asarray(request.get_json()['barcode'])
        raw = get("https://www.google.com/search?q={0}".format(barcode)).text
        page = fromstring(raw)

        product_name = None
        for result in page.cssselect("div"):
            if result.cssselect("a"):
                url = result.cssselect("a")[0].get("href")
                if url.startswith("/url?"):
                    product_name = result.cssselect("a")[0].cssselect("div")[0].text_content()
                    break

        return make_response(jsonify({'product': product_name, 'timestamp': timestamp}))


api.add_resource(AddProduct, '/add_product')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=3500)
