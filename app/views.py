from flask import Flask, jsonify, abort, make_response, request, render_template
from flask_restful import  reqparse

NOT_FOUND = 'Not found'
BAD_REQUEST = 'Bad request'

app = Flask(__name__)
orders = [] 

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
    if orders:
        return jsonify({'orders': orders}),200
    else: abort(404)    

@app.route('/api/v1/orders/<int:id>', methods=['GET'])
def get_order(id):
    if orders:
        order = _get_order(id)
        if not order:
            abort(404)
        return jsonify({'order': order}),200
    else: abort(404)

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
    parser.add_argument("status",
            type=int)
    data = parser.parse_args()
    orders.append(data)
    return jsonify({'order': data}), 200

@app.route('/api/v1/orders', methods=['PUT'])
def update_order():
    parser = reqparse.RequestParser()
    parser.add_argument("id",
            type=int,
            required=True,
    )
    parser.add_argument("status",
            type=int,
            required=True,
    )
    data = parser.parse_args()
    status = data['status']
    if type(status) is not int:
        abort(400)                         
    for order in orders:
        if order['id']==data['id']:
            order['status']=data['status']
            return jsonify({'order': order},200)
        else: abort(404)    

@app.route('/api/v1/orders', methods=['DELETE'])
def delete_order():
    parser = reqparse.RequestParser()
    parser.add_argument("id",
            type=int,
            required=True,
    )
    data = parser.parse_args()
    if orders:
        for i,order in enumerate(orders):
            if order['id']==data['id']:
                del_order=order
                del  orders[i]
                return jsonify({'order': del_order},200)
            else: abort(404)
    else:
        return jsonify({'error': 'No Items Left'},200)

if __name__ == '__main__':
    main()