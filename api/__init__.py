
from flask_restful import Api
from .Task import Task
from .TaskBYID import TaskBYID
from app import flaskAppInstance


restServer=Api(flaskAppInstance)
restServer.add_resource(Task, "/api/v1.0/task")
restServer.add_resource(TaskBYID,"/api/v1.0/task/id/<string:taskId>")
