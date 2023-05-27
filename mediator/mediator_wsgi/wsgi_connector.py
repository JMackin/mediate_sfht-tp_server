import mediator


class WsgiConnector(object):

    def __call__(self, environ, start_fn):
        start_fn('200 OK', [('Content-Type', 'text/plain')])
        yield "Hello World!\n"


app = mediator.mediator.wsgi


# ***
# Gunicorn basic usage
#
#       gunicorn [OPTIONS] [WSGI_APP]
#
# Run server from mediator_wsgi/ with:
#
#       gunicorn mediator_wsgi.wsgi_connector:WsgiConnector
#
#       gunicorn --print-config --chdir ~/Code/Python/mediate_http-sftp \
#       mediator_wsgi.wsgi_connector --check-config
# ***

