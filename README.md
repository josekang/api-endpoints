[![Maintainability](https://api.codeclimate.com/v1/badges/1a4287304b94cdf7443e/maintainability)](https://codeclimate.com/github/josekang/api-endpoints/maintainability)  [![Coverage Status](https://coveralls.io/repos/github/josekang/api-endpoints/badge.svg)](https://coveralls.io/github/josekang/api-endpoints)  [![Build Status](https://travis-ci.org/josekang/api-endpoints.svg?branch=develop)](https://travis-ci.org/josekang/api-endpoints)  [![Test Coverage](https://api.codeclimate.com/v1/badges/1a4287304b94cdf7443e/test_coverage)](https://codeclimate.com/github/josekang/api-endpoints/test_coverage) ![Heroku App Status](http://heroku-badge.herokuapp.com/?app=our-api-heroku-deploy-app-flas&root=/api/v1/orders/)![GitHub issues](https://img.shields.io/github/issues/josekang/api-endpoints.svg)

# api-endpoints

The following files shows a set of API endpoints already. 

The API endpoints use data structures to store data in memory.

The app uses flask microframework as the server side. We install flask through:
    - pip install flask
    
The app uses pylint which is a linting library for python. We install pylint through:
    - pip install pylint
    
The app also uses a PEP8 Style Guide. This style guide simply is some of the key points that you can use to make your code more organized and readable.
    - pip install pep8
    
The app uses a Testing Framework specifically "pytest" which is a python testing framework that tests our endpoints codes. We can install through:
    - pip install pytest
    
The API endpoints do the following using data structures:
    - Place a new order for food.
    - Get a list of orders.
    - Fetch a specific order.
    - Update the order status.

After setting up the endpoints, i run the tests codes through postman to make sure the endpoints do the specified tasks.

The API endpoints test for the following :
     GET /orders - Get all the orders.
     GET /orders/<orderId> - Fetch a specific order.
     POST /orders- Place a new order.
     PUT /orders/<orderId> - Update the status of an order.
    
    
    



     


 


