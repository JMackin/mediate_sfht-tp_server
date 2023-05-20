class WsgiConnector(object):

    def __call__(self, environ, start_fn):
        start_fn('200 OK', [('Content-Type', 'text/plain')])
        yield "Hello World!\n"


app = WsgiConnector()
