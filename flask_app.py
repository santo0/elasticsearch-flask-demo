from flask import Flask
from api.elastic_test import connect_elasticsearch

es = connect_elasticsearch()
app = Flask(__name__)

from api.retrieve_data import *
from api.insert_data import *

if __name__ == '__main__':
    app.run(port=5000, debug=True)
