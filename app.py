from flask import Flask, render_template
import json

app = Flask(__name__)

def load_pets():
    with open("data/pets.json") as file:
        return json.load(file)

@app.route("/")
def home():
    pets = load_pets()
    return render_template("index.html", pets=pets)

if __name__ == "__main__":
    app.run(debug=True)