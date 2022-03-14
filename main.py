from flask import Flask, request, Response
import json

app = Flask(__name__)

# KEY: VALUE
animals_db = {
    "1": { "name": "Lion", "description": "yellow with a mane "}, 
    "2": { "name": "Flamingo", "description": "pink with two legs"}
}


@app.route("/")
def hello():
    return "Welcome to Atlanta Zoo"

@app.route("/animals")
def list_animals():
    return animals_db

@app.route("/animals/<animal_id>")
def get_animal(animal_id):
    return animals_db[animal_id]

@app.route("/animals/add", methods=['POST'])
def add_animal():
    req_data = request.get_json()
    
 
 #Extract the animal data from the request 
    new_animals = req_data['animal']

    #Get the last position in the database
    new_id = len(animals_db) + 1

    #Create a new entry for my animal
    new_animal_data = {str(new_id) : new_animals }

    #Update the database with the new entry
    animals_db.update(new_animal_data)

    return "The animal was successfully added"





#Update an existing animal

@app.route("/animals/update", methods=["POST" ])
def update_animal():
    req_data = request.get_json()

    #Create a new update to animal 


    #Update the database with the new entry
    animals_db.update(req_data)
    return "The animal has been updated"






if __name__== "__main__":
    app.run(host="127.0.0.1")




######################

