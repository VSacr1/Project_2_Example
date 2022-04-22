from application import app 
from flask import Flask, request, Response
import requests


@app.route('/', methods=['GET'])
def home(): 
    character_api = requests.get('http://character_api:5000/get_character')
    class_api = requests.get('http://class_api:5000/get_class')
    return Response(f"{character_api.text} {class_api.text}", mimetype="text/plain")