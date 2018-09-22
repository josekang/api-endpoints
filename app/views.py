from flask import Flask, jsonify, abort, make_response, request, render_template
from flask_restful import  reqparse

NOT_FOUND = 'Not found'
BAD_REQUEST = 'Bad request'

app = Flask(__name__)
orders = [
    {
        'id': 1,
        'name': 'vegetables',
        'value': 1000,
        'status': 0
    },
    {
        'id': 2,
        'name': 'refreshments',
        'value': 300,
        'status': 0
    },
    {
        'id': 3,
        'name': 'fruits',
        'value': 20,
        'status': 0
    },
]

def _get_order(id):
    return [order for order in orders if order['id'] == id]

def _record_exists(name):
    return [order for order in orders if order["name"] == name]

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': NOT_FOUND}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': BAD_REQUEST}), 400)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/v1/orders', methods=['GET'])
def get_orders():
    return jsonify({'orders': orders})


@app.route('/api/v1/orders/<int:id>', methods=['GET'])
def get_order(id):
    order = _get_order(id)
    if not order:
        abort(404)
    return jsonify({'orders': order})


@app.route('/api/v1/orders', methods=['POST'])
def create_order():
    parser = reqparse.RequestParser()
    parser.add_argument("id",
            type=int, 
            required=True,
    )
    parser.add_argument("name",
            type=str,
            required=True,
    )
    parser.add_argument("value",
            type=int,
            required=True,
    )
    parser.add_argument("status",type=int,
            required=True)
    data = parser.parse_args()
    order = {"id": data['id'], "name": data['name'],
            "value": data['value'],"status": data['status']}
    orders.append(order)
    return jsonify({'order': order}), 201


@app.route('/api/v1/orders/<int:id>', methods=['PUT'])
def update_order(id):
    parser = reqparse.RequestParser()
    parser.add_argument("status",
            type=int,
            required=True,
    )
    data = parser.parse_args()
    status = data['status']
    if type(status) is not int:
        abort(400)
    orders[id]['status'] = status
    order = {"id":id, "name": orders[id]['name'],
        "value":orders[id]['value'],"status": orders[id]['status']}
    return jsonify({'order': order}), 201


@app.route('/api/v1/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    if orders and id<len(orders):
        order=orders[id]
        del orders[id]
        return jsonify({'order': order}), 201
    else:
        return jsonify({'error': "no items left"}), 404

