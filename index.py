import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler)
        # write your code here
    ])

    port = 1337
    app.listen(port)
    print(f"Application is ready on port {port}")
    tornado.ioloop.IOLoop.current().start()