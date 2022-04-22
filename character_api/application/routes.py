from application import app 
from flask import Flask, request, Response 
import random

@app.route('/get_character',methods=['GET'])
def name(): 
    character_choice = ["Tiefling", "Human", "Orc", "Elf", "Aasamar" ]
    character_name = random.choice(character_choice)
    return Response(f"{character_name}", mimetype="text/plain")