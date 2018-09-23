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
        self.assertEqual(response.status_code, 404)

    def test_get_one(self):
        response = self.app.get(BASE_URL+'/3')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 404)
    
    def test_post_one(self):
        data = {
        'id': '1',
        'name': 'the name',
        'value':'33432'
        }
        response=self.app.post(BASE_URL, 
                       data=json.dumps(data),
                       content_type='application/json')
        anyname = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)

    def test_get_one_two(self):
        data = {
        'id': '1',
        'name': 'the name',
        'value':'33432'
        }
        first_response=self.app.post(BASE_URL, 
                       data=json.dumps(data),
                       content_type='application/json')
        response = self.app.get(BASE_URL+'/1')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)

    def test_not_get_one(self):
        data = {
        'id': '1',
        'name': 'the name',
        'value':'33432'
        }
        first_response=self.app.post(BASE_URL, 
                       data=json.dumps(data),
                       content_type='application/json')
        response = self.app.get(BASE_URL+'/2')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 404)
     
    def test_order_not_exist(self):
        response = self.app.get(BAD_ORDER_URL)
        self.assertEqual(response.status_code, 404)

    def test_update(self): 
        client = app.test_client(self)
        self.new_orders={"id": 1, "status": 0}
        self.old_edit= {"id": 1, "status":1  }
        data = client.put(BASE_URL+'/1',
                                 data = json.dumps(self.new_orders), 
                                 content_type="application/json")
        order = client.get(BASE_URL+'/1',
                             content_type="application/json")
        self.assertEqual(order.status_code, 200)
           
    def test_update_error(self):
        # cannot edit non-existing item
        order = {"value": 30}
        response = self.app.put(BAD_ORDER_URL,
                                data=json.dumps(order),
                                content_type='application/json')
        self.assertEqual(response.status_code, 405)

    def test_delete(self):
        response = self.app.delete(BASE_URL + '/0',
                                content_type='application/json')
        self.assertEqual(response.status_code,405)
        response = self.app.delete(BAD_ORDER_URL)
        self.assertEqual(response.status_code, 405)

    def tearDown(self):
        # reset app.items to initial state
        orders = self.backup_orders

if __name__ == "__main__":
    unittest.main() 