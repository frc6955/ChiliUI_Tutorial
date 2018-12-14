# Should return 2 tasks
echo "Testing tasks"
curl -i http://localhost:5000/todo/api/v1.0/tasks
# Should return task 1
echo "Testing task 1"
curl -i http://localhost:5000/todo/api/v1.0/tasks/1
# Should return task 2
echo "Testing task 2"
curl -i http://localhost:5000/todo/api/v1.0/tasks/2
# Should return 404 with JSON payload
echo "Testing task not found"
curl -i http://localhost:5000/todo/api/v1.0/tasks/3
# Should return 201 with JSON payload of created task
echo "Testing task creation"
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks
# Should return 3 tasks
echo "Testing successful task creation"
curl -i http://localhost:5000/todo/api/v1.0/tasks
# Should delete task 2
echo "Testing task deletion"
curl -i -H "Content-Type: application/json" -X DELETE localhost:5000/todo/api/v1.0/tasks/2
# Should return 2 tasks: 1 and 3
echo "Testing successful task deletion"
curl -i http://localhost:5000/todo/api/v1.0/tasks