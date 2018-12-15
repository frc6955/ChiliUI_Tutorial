# Flask REST API and Plotly streaming

This example takes the basic principles from the REST API example and the setInterval example and combines them to create a real-time Plotly plot. The JS code used is taken from the Plotly.JS examples, found in the [streaming section](https://plot.ly/javascript/streaming/).


To run the code, run
```python
python main.py
```
in the terminal and direct your browser to [localhost:5000](http://localhost:5000). If you want to see the API in action, go to [localhost:5000/api/get_state](http://localhost:5000/api/get_state). Upon refreshing, a new number will be sent, just as in the setInterval example.


This code takes the setInterval function and uses the callback to generate a jQuery getJSON call, which requests the state from the API, logs it (console and a *div* element) and then concatenates the new value to the plot array. It then updates the Plotly graph. Notice how the script is placed at the end of the HTML code, so that the DOM already contains a reference to the `#graph` div.

---

## Important
This is one way of achieving dynamic plots. However, in case of the `/api/get_state` requests, these can take anywhere from 4 to 8 ms, with observed peaks of 19 ms. This indicates that it would be much better to open a websocket connection between the site and Flask and then generate *request* events with the `setInterval` function. These requests would then trigger the server to prepare the data and generate a *response* event, which would be captured by the site, processed and then the Plotly graph would be updated.