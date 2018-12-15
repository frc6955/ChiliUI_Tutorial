# Code examples for ChiliUI

In this repo, you will find various examples of Flask code for different tasks necessary for writing the Web UI program. Flask is a web microframework for Python, ideal for writing and serving small scale sites.

The examples currently included in this repo are:
* [Flask with Plotly.JS](https://github.com/frc6955/ChiliUI_Tutorial/tree/master/flask_plotly_example)
* [REST API with Flask](https://github.com/frc6955/ChiliUI_Tutorial/tree/master/flask_rest-api_example)
* [Websockets with Flask](https://github.com/frc6955/ChiliUI_Tutorial/tree/master/flask_sockets_example)
* [Plotly.JS with Flask]() (WIP)
---
The ChiliUI is intended for realtime monitoring and debugging of the robot state. It must be based on a Flask backend, with a Websocket connection to a website running Plotly.JS for data visualization and Websockets for real-time updates. The backend must open a REST API for state querying as well as POST requests from the robot, with which the server logs are updated. A desired feature is a broadcasted notes section, where information may be recorded and stored server side. Finally, data transmission should be via JSON, however logging and storage on the server must be via CSV in case of power failures to the robot.