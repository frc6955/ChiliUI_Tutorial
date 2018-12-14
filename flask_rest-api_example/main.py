from flask import Flask, jsonify, abort, make_response, request, url_for

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Find tutorial',
        'done': False
    }
]

# Auxiliary function used by /.../tasks route to convert id field for any task into a URI
def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

# Overwritten 404 error handler. Without this, a 404 returns HTML, but the client always expects JSON
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# Method to create tasks. ID of new task is the ID of the last task + 1. Description is not neccesary. Returns 201 if succesful
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

# Method to update task via a POST to task id. Conditionals are for error checking.
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = [task for tassk in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) is not unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

# Method to delete a task upon receiving a DELETE request to a task id URI
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

# Method to retrieve task from id
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task =  [task for task in tasks if task['id'] == task_id]
    if len(task) == 0: abort(404)
    return jsonify({'tasks': task[0]})

# Method to get all tasks in database
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})

if __name__ == '__main__':
    app.run(debug=True)