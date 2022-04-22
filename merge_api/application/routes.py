from application import app 
from flask import Flask, request, Response 

@app.route('/get_stats', method=['POST'])
def effect(): 
    stat_data = request.get_json 
    character_name = stat_data["Character"]
    class_name = stat_data["Class"]
    stats = {"Ranger" : "Dexterity", "Sorcerer" : "Wisdom", "Wizard" : "Intelligence", "Rogue" : "Dexterity", "Bard":"Charisma", "Barbarian":"Strength"}