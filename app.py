from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"slackUsername": "Joseun",
                    "backend": True,
                    "age": 27,
                    "bio": "Hi, Joseph Ologunja here, I am a Full Stack developer, proficient in Python"
                   })
