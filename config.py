import os
from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config['MONGO_DBNAME'] = "MAYUR_DANCE_ACADEMY"
app.config['MONGO_URI'] = "mongodb://localhost:27017/REGISTRATIONS"
mongo = PyMongo(app)
