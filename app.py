from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

templates = [
    {
        "inputs" : 9,
        "category" : "K-POP BOY GROUP",
        "word" : "Straykids"
    },
    {
        "inputs" : 6,
        "category" : "GAME",
        "word" : "Roblox"
    },

]

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/get-template")
def get_template():
  return jsonify({
        "status": "success",
        "word": random.choice(templates)
  })

if __name__ == '__main__':
  app.run()
