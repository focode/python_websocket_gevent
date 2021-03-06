from geventwebsocket import WebSocketServer, WebSocketApplication, Resource

class EchoApplication(WebSocketApplication):
    def on_open(self):
        print ("Connection opened")

    def on_message(self, message):
        print(dir(self.ws))
        self.ws.send(message)

    def on_close(self, reason):
        print (reason)

class EchoApplication1(WebSocketApplication):
    def on_open(self):
        print ("Connection opened")

    def on_message(self, message):
        print(dir(self.ws))
        self.ws.send(message)

    def on_close(self, reason):
        print (reason)

WebSocketServer(('', 8000), Resource({'/': EchoApplication})).serve_forever()
