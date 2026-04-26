from flask import Flask, render_template
import json

app = Flask(__name__)

def load_pets():
    with open("data/pets.json") as file:
        return json.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/browse")
def browse():
    pets = load_pets()
    return render_template("browse.html", pets=pets)

@app.route("/animal/<int:pet_id>")
def animal_detail(pet_id):
    pets = load_pets()

    for pet in pets:
        if pet["id"] == pet_id:
            return render_template("animal.html", pet=pet)

    return "Pet not found"

@app.route("/match/<int:pet_id>")
def match_pet(pet_id):
    pets = load_pets()

    for pet in pets:
        if pet["id"] == pet_id:
            return render_template("match.html", pet=pet)

    return "Pet not found"

if __name__ == "__main__":
    app.run(debug=True)