import gevent
from gevent.pywsgi import WSGIServer
from gevent.lock import Semaphore
from geventwebsocket.handler import WebSocketHandler
from datetime import datetime

def process(ws,data,sem):
    print('{} got data "{}"'.format(datetime.now().strftime('%H:%M:%S'), data))
    # gevent.sleep(1)
    with sem:
        ws.send(data)

def app(environ, start_response):
    ws = environ['wsgi.websocket']
    sem = Semaphore()
    while True:
        data = ws.receive()
        gevent.spawn(process,ws,data,sem)

server = WSGIServer(("", 10004), app,handler_class=WebSocketHandler)
server.serve_forever()
