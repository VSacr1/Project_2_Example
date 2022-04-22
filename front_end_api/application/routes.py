from application import app 
from flask import Flask, request
import requests


@app.route('/', methods=['GET'])
def home(): 
    character_api = requests.get('http://character_api:5000/get_character')
    class_api = requests.get('http://class_api:5000/get_class')
    return f"{character_api} {class_api}"