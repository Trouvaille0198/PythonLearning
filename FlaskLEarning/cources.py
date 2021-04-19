from flask import Flask, request, jsonify, abort, redirect, session

app = Flask(__name__)
app.secret_key = '123'


@app.route('/')
def hello_world():
    return 'Hello, World!'


# app.run(debug=True)
app.run(debug=True)
