from bottle import run, route,  static_file, request, post
from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
data = {'logged_in': False, "first_name": '', "last_name": ''}


@route('/')
def index():
    if data['logged_in']:
        template = env.get_template('main.html')
        my_html = template.render(
            {'first_name': data['first_name'], 'last_name': data['last_name']})

    else:
        template = env.get_template('login_page.html')
        my_html = template.render()

    return my_html


@post('/log_in_attempt')
def log_in_attempt():
    data['first_name'] = request.forms.get('firstName')
    data['last_name'] = request.forms.get('lastName')
    data['logged_in'] = True
    template = env.get_template('main.html')
    return template.render({'first_name': data['first_name'], 'last_name': data['last_name']})


@route('<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')


run(host='localhost', port=7000)
