from chalice import Chalice
from chalice.app import Response

app = Chalice(app_name='chalice-uuid-service')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/uuid')
def get_uuid():
    import uuid
    n = 1
    qs = app.current_request.query_params
    try:
        if "n" in qs:
            n = int(qs["n"])
    except TypeError:
        pass
    uuids = []
    for i in range(n):
        uuids.append(str(uuid.uuid4()))
    body = {
        "uuid": uuids
    }
    response = Response(
        body,
        headers={'Content-Type': 'application/json'}
    )
    return response
