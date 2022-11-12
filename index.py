import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        # write your code here
        self.write("something")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler)
    ])

    port = 1337
    app.listen(port)
    print(f"Application is ready on port {port}")
    tornado.ioloop.IOLoop.current().start()