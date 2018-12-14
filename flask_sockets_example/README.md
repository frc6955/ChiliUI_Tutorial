# Flask with Websockets

Example based on article *Easy WebSockets with Flask and Gevent* written by Miguel Grinberg (February 10, 2014). The article can be found in [this link](https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent).


To run the code, run
```python
python main.py
```
in the terminal and direct your browser to [localhost:5000](http://localhost:5000). This will load a plain HTML page. The site attemps a connection upon loading, triggering a *connection* event, which is handled and printed by the server. The page includes two forms, *echo* and *broadcast*. Both forms generate different WS events which are handled by different event handlers on the server. 

However, both handlers then `emit` a *response* event, which is handled by the page by appending the contents of the *response* event to a `div`.
The difference between forms is that the *echo* forms trigger a normal `emit` from the server, however the *broadcast* form triggers an `emit` with a `broadcast=True` parameter. This causes all currently connected clients to receive the *response* event.

To handle the forms, jQuery is used to intercept the forms submit event with the following syntax:
```javascript
$('form#form_id').submit(function(event) {
    var form_data = $('#input_text_id').val();
    // Do something with form_data
});
```

Finally, a `namespace` variable is declared in both the JS client and the python server. This namespace allows multiple namespace sessions to occur within a single server.