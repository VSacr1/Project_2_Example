from application import app 
from flask import Flask, request, Response 
import random

@app.route('/get_character',methods=['GET'])
def name(): 
    class_choice = ["Tiefling", "Human", "Orc", "Elf", "Aasamar" ]
    event_name = random.choice(class_choice)