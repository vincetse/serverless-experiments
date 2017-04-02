from chalice import Chalice
from chalice.app import Response
import urlparse

app = Chalice(app_name='chalice-uuid-service')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/uuid')
def get_uuid():
    import uuid
    n = 1
    qs = app.current_request.query_params
    if "n" in qs:
        n = int(qs["n"])
    uuids = []
    for i in xrange(n):
        uuids.append(str(uuid.uuid4()))
    body = {
        "uuid": uuids
    }
    response = Response(
        body,
        headers={'Content-Type': 'application/json'}
    )
    return response
