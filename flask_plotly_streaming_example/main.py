from flask import Flask, render_template, jsonify
import plotly
import plotly.plotly as py 
import plotly.graph_objs as go
import numpy as np
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

# API call to simulate a state. Returns a payload with ID=1 and val=a random number
@app.route('/api/get_state', methods=['GET'])
def get_state():
    rand_number = float(np.random.randn(1))
    payload = [{'id': 1, 'val': rand_number}]
    return jsonify(payload)

if __name__ == '__main__':
    app.run(debug=True)