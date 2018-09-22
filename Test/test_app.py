from copy import deepcopy
import unittest
import json

from app.views import app,orders


BASE_URL = 'http://127.0.0.1:5000/api/v1/orders'
BAD_ORDER_URL = '{}/5'.format(BASE_URL)
GOOD_ORDER_URL = '{}/3'.format(BASE_URL)

class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        self.backup_orders = deepcopy(orders)  
        self.app = app.test_client()
        self.app.testing = True

    def test_get_all(self):
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['orders']), 2)

    def test_get_one(self):
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['orders'][0]['name'], 'refreshments')

    def test_order_not_exist(self):
        response = self.app.get(BAD_ORDER_URL)
        self.assertEqual(response.status_code, 404)

    def test_update(self):
        order = {"status": 1}
        response = self.app.put(BASE_URL+'/1',
                                data=json.dumps(order),
                                content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data())
        self.assertEqual(data['order']['status'], 1)
       
    def test_update_error(self):
        # cannot edit non-existing item
        order = {"value": 30}
        response = self.app.put(BAD_ORDER_URL,
                                data=json.dumps(order),
                                content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_delete(self):
        response = self.app.delete(BASE_URL+'/0',
                                content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.app.delete(BAD_ORDER_URL)
        self.assertEqual(response.status_code, 404)

    def tearDown(self):
        # reset app.items to initial state
        orders = self.backup_orders

if __name__ == "__main__":
    unittest.main() 