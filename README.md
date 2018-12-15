# Code examples for ChiliUI

In this repo, you will find various examples of Flask code for different tasks necessary for writing the Web UI program. Flask is a web microframework for Python, ideal for writing and serving small scale sites.

The examples currently included in this repo are:
* [Flask with Plotly.JS](https://github.com/frc6955/ChiliUI_Tutorial/tree/master/flask_plotly_example)
* [REST API with Flask](https://github.com/frc6955/ChiliUI_Tutorial/tree/master/flask_rest-api_example)
* [Websockets with Flask](https://github.com/frc6955/ChiliUI_Tutorial/tree/master/flask_sockets_example)
* [Plotly.JS with Flask]() (WIP)
---

The ChiliUI is intended for realtime monitoring and debugging of the robot state. It must be based on a Flask backend, with a Websocket connection to a website running Plotly.JS for data visualization and Websockets for real-time updates. The backend must open a REST API for state querying as well as POST requests from the robot, with which the server logs are updated. A desired feature is a broadcasted notes section, where information may be recorded and stored server side. Finally, data transmission should be via JSON, however logging and storage on the server must be via CSV in case of power failures to the robot.

---

El ChiliUI es un software ideado para el monitoreo y debuggeo en tiempo real del robot. Debe estar basado en un *backend* Flask, con una conexion Websockets a una pagina corriendo Plotly.JS para visualizacion de datos y Websockets para actualizaciones en tiempo real. El *backend* debe implementar un API REST para solicitar el estado y permitir solicitudes POST desde el robot para actualizar los logs del servidor. Una feature deseado pero no esencial es un bloc de notas con *broadcasting* que sea registrado y almacenado en el servidor. Finalmente, la transmision de datos debiese ser mediante JSON, sin embargo el almacenimienot de datos en el servidor debe ser mediante CSV en caso de fallas de poder.