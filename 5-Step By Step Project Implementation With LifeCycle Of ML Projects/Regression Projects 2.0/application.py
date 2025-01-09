from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Flask App Initialization
application = Flask(__name__)
app = application

# Importing the model and the scaler
model = pickle.load(open('models/ridge_model.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

# Run the app on the local server
if __name__ == '__main__':
    app.run(host='0.0.0.0')