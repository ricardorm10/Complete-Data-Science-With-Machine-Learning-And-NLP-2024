from flask import Flask, request, render_template
import pickle

# Flask App Initialization
application = Flask(__name__)
app = application

# Importing the model and the scaler
model = pickle.load(open('models/ridge_model.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

# Route for the index
@app.route('/')
def index():
    return render_template('index.html')

# Route for the prediction
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the data from the form
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))
        
        # Scale the data
        data_scaled = scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        result = model.predict(data_scaled)
        
        # Return the result
        return render_template('home.html', result=result[0])
    else:
        return render_template('home.html')

# Run the app on the local server
if __name__ == '__main__':
    app.run(host='0.0.0.0')