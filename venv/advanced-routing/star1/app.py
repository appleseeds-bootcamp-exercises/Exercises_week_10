from bottle import run, route, error, static_file


@route('/')
def index():
    return "Let's pretend this is a normal landing page"


@route('/<filename:path>')
def image404(filename):
    print('oho')
    return static_file(filename, root='static')


@error(404)
def error_404(error):
    return static_file('error.html', root='static')


if __name__ == "__main__":
    run(host='localhost', port='7000', reloader=True)
