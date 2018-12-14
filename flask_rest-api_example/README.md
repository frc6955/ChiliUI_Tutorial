# Flask REST API

Example based on article *Designing a RESTful API with Python and Flask* written by Miguel Grinberg (May 20, 2013). The article can be found in [this link](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask).


To run the code, run
```python
python main.py
```
in the terminal and direct your browser to [localhost:5000/todo/api/v1.0/tasks](http://localhost:5000/todo/api/v1.0/tasks). This will return a JSON file which will be pretty-printed by your browser. To test the API, a shell script has been included, `test_api`. In case that `test_api.sh` is not included in the directory or you're receiving a `curl: (3) Illegal characters found in URL` error, run the following commands in this directory:
```shell session
tr -d '\r' < test_api_file.sh > test_api.sh
chmod +x test_api.sh
```
The first commands will fix the URLs in the shell file and the second will make the shell script executable. The tests depend on `curl`, so in case of receiving a command not found error, install it with `sudo apt-get install curl`.