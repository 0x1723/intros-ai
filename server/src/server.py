import tornado.ioloop
import tornado.web
from tasks import TasksHandler, TaskHandler

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write(f"Hello, world. Nothing to see here on this endpoint. The endpoints available are /tasks and /tasks/[id]")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/tasks", TasksHandler),
        (r"/tasks/\d+", TaskHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
