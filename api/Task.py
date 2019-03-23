from flask_restful import Resource
import logging as logger


class Task(Resource):
    def get(self):
        logger.debug("Inside a get method")
        return {"message": "inside get method"},200

    def post(self):
        logger.debug("Inside a post method")
        return {"message":"inside post method"},200

    def put(self):
        logger.debug("Inside a put method")
        return {"message":"inside a put method"},200

    def delete(self):
        logger.debug("Inside a delete method")
        return {"message":"insode a delete method"},200
