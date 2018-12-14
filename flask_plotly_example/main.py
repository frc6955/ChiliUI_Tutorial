from flask import Flask, render_template
import plotly
import plotly.plotly as py 
import plotly.graph_objs as go
import numpy as np
import json


app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome!"

@app.route('/lc')
def line():
    count = 500
    x_scale = np.linspace(0, 100, count)
    y_scale = np.random.randn(count)

    trace = go.Scatter(x = x_scale, y = y_scale)
    graphJSON = json.dumps([trace], cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html', graphJSON=graphJSON)

@app.route('/mlc')
def multi_line():
    count = 500
    lines = 3
    x_scale = np.linspace(0, 100, count)
    y_scales = [np.random.rand(count) for _ in range(lines)]

    traces = [go.Scatter(x=x_scale, y=ys) for ys in y_scales]
    graphJSON = json.dumps(traces, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html', graphJSON=graphJSON)

if __name__ == "__main__":
    app.run()