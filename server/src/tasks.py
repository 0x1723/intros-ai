import tornado.web
from database import select
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
