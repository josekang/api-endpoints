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
            return jsonify({'message':"Order does not exist"}),404
        return jsonify({'order': order}),200
    else: abort(404)

@app.route('/api/v1/orders', methods=['POST'])
def create_order():
    parser = reqparse.RequestParser()
    parser.add_argument("name",
            type=str,
            required=True
    )
    parser.add_argument("value",
            type=int,
            required=True
    )
    parser.add_argument("status",
            type=str)
    data = parser.parse_args()
    id = (len(orders))+1
    data['id']=id
    orders.append(data)
    return jsonify({'order': data}), 201

@app.route('/api/v1/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    parser = reqparse.RequestParser()
    parser.add_argument("status",
            type=str,
            required=True,
    )
    
    data = parser.parse_args()
    status = data['status']
    if type(status) is not str:
        return jsonify({'message':"Make sure the status is a string."}), 400                   
    for order in orders:
        if order['id']==order_id:
            order['status']=status
            return jsonify({'order': order},200)
        return jsonify({'message':"order does not exist."}),404

@app.route('/api/v1/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    if order_id:
        for order in orders:
            if order['id']==order_id:
                orders.remove(order)
                return jsonify({'message':"Order successfully deleted."}),200
            return jsonify({'message':"order does not exist."}),404
    
    if __name__ == '__main__':
         app.run(debug=True)