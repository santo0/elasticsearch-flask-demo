
from flask_app import app
from api.elastic_test import connect_elasticsearch
from flask import jsonify, request

es = connect_elasticsearch()


@app.route('/', methods=['GET'])
def home():
    message = 'Flask is UP and RUNNING'
    return jsonify(message)


@app.route('/get_user', methods=['GET'])
def get_user():
    content = request.json
    user_id = content['id']
    results = es.get(index='user', id=user_id)
    return jsonify(results['_source'])

@app.route('/search_user', methods=['GET'])
def search_user():
    content = request.json
    keyword = content['keyword']

    query_body = {
        "query": {
            "match": {
                "name": keyword
            }
        }
    }

    res = es.search(index="user", body=query_body)

    return jsonify(res['hits']['hits'])
