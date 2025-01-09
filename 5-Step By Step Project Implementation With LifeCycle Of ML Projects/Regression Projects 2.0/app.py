from Flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    