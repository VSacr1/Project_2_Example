from application import app 
from flask import Flask, request, Response 
import random

@app.route('/get_class',methods=['GET'])
def name(): 
    class_choice = ["Ranger", "Sorcerer", "Wizard", "Rogue", "Bard", "Barbarian"]
    class_name = random.choice(class_choice)
    return Response(f"{class_name}", mimetype="text/plain")