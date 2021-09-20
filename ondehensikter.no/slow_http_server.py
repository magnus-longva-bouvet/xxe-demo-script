from tornado.ioloop import IOLoop
import tornado.web
import time
import os
CURRENT_DIR = os.path.abspath(os.getcwd())
print(f"current dir is {CURRENT_DIR}")


class MainHandler(tornado.web.RequestHandler):
    def get(self):

        with open(f"{CURRENT_DIR}/jar.jar","rb") as file:
            print("serving jar")
            self.write(file.read())
            self.flush()
            print("waiting and never closing connection.")
            time.sleep(99999)
            self.finish()


if __name__ == "__main__":
    application =  tornado.web.Application([
        (r'/', MainHandler),
        (r'/jar.jar', MainHandler),
    ])
    port = 9999
    application.listen(port)
    print("Listening on port "+str(port))
    IOLoop.instance().start()