from bottle import run, route, jinja2_view
data = {'counter': 1}


@route('/')
@jinja2_view('base.html',  template_lookup=['templates'])
def index():
    data['counter'] += 1
    return {'counter': data['counter']}

run(host='localhost', port=7000)
