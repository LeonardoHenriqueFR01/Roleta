from flask import Flask


app = Flask(__name__) # Meu app flask

from app import routes
