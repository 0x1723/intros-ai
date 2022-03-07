import tornado.web
from database import insert, select, delete
import json
import traceback

class TasksHandler(tornado.web.RequestHandler):
    
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        try:
            rows = select("tasks")
            self.write(json.dumps(rows))
        except Exception as e:
            self.write(traceback.format_exc())

    def post(self):
        try:
            data = tornado.escape.json_decode(self.request.body)
            if "description" not in data:
                raise Exception("The data posted needs to have a description key")
            insert("tasks", ["description"], [data["description"]])
            self.write("Task {} added!".format(data["description"]))
        except Exception as e:
            self.write(traceback.format_exc())

    def options(self):
        pass

class TaskHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With")
        self.set_header('Access-Control-Allow-Methods', 'DELETE, POST, OPTIONS')

    def delete(self):
        try:
            task_id = int(self.request.path.replace("/tasks/", ""))
            rows = delete("tasks", task_id)
            self.write(json.dumps(rows))
        except Exception as e:
            self.write(traceback.format_exc())

    def options(self):
        pass
