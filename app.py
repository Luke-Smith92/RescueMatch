from flask import Flask, render_template, session, redirect, url_for
import json

app = Flask(__name__)
app.secret_key = "rescuematch-secret-key"

def load_pets():
    with open("data/pets.json") as file:
        return json.load(file)

def get_matches_left():
    if "matches_left" not in session:
        session["matches_left"] = 10
    return session["matches_left"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/browse")
def browse():
    pets = load_pets()
    matches_left = get_matches_left()
    return render_template("browse.html", pets=pets, matches_left=matches_left)

@app.route("/animal/<int:pet_id>")
def animal_detail(pet_id):
    pets = load_pets()

    for index, pet in enumerate(pets):
        if pet["id"] == pet_id:
            previous_pet = pets[index - 1] if index > 0 else None
            next_pet = pets[index + 1] if index < len(pets) - 1 else None

            return render_template(
                "animal.html",
                pet=pet,
                previous_pet=previous_pet,
                next_pet=next_pet
            )

    return "Pet not found"

@app.route("/match/<int:pet_id>")
def match_pet(pet_id):
    pets = load_pets()
    matches_left = get_matches_left()

    if matches_left <= 0:
        return render_template("no_matches.html")

    session["matches_left"] -= 1

    for pet in pets:
        if pet["id"] == pet_id:
            return render_template("match.html", pet=pet, matches_left=session["matches_left"])

    return "Pet not found"

if __name__ == "__main__":
    app.run(debug=True)