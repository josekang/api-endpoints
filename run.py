# run.py
# This simply launches our app server

from flask import Flask
from app.views import app


app.run()