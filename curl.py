import os 

tests = """
# get orders
curl -i http://127.0.0.1:5000/api/v1/orders
# order 1
curl -i http://127.0.0.1:5000/api/v1/orders/1
# order 2
curl -i http://127.0.0.1:5000/api/v1/orders/2
# err: non-existing order
curl -i http://127.0.0.1:5000/api/v1/orders/4
# err: add order already in orders
curl -i -H "Content-Type: application/json" -X POST -d  '{"name":"fresh juice", "value": 120}' http://127.0.0.1:5000/api/v1/orders
# err: add order with value not int 
curl -i -H "Content-Type: application/json" -X POST -d  '{"name":"delicious vegetables", "value": "200"}' http://127.0.0.1:5000/api/v1/orders
# add order with proper values
curl -i -H "Content-Type: application/json" -X POST -d  '{"name":"offer", "value": 1529}' http://127.0.0.1:5000/api/v1/orders
# show orders
curl -i http://127.0.0.1:5000/api/v1.0/orders
# err: edit non-existing order
curl -i -H "Content-Type: application/json" -X PUT -d '{"value": 300}' http://127.0.0.1:5000/api/v1/orders/5
# OK: edit existing order
curl -i -H "Content-Type: application/json" -X PUT -d '{"value": 300}' http://127.0.0.1:5000/api/v1/orders/3
# show orders
curl -i http://127.0.0.1:5000/api/v1/orders
# err: delete non-existing order
curl -i -H "Content-Type: application/json" -X DELETE http://127.0.0.1:5000/api/v1/orders/5
# OK: delete existing order
curl -i -H "Content-Type: application/json" -X DELETE http://127.0.0.1:5000/api/v1/orders/3
# show orders
curl -i http://127.0.0.1:5000/api/v1/orders
"""

for line in tests.strip().split('\n'):
    print('\n{}'.format(line))
    if not line.startswith('#'):
        cmd = line.strip() 
        os.system(cmd)