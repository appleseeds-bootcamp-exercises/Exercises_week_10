from bottle import route, run, static_file
import json
import random


@route('/')
def index():
    return static_file("index.html", root='static')

@route('/css/<filename:re:.*\.css>')
def css_files(filename):
    return static_file(filename, root='static/css')

@route('/js/<filename:re:.*\.js>')
def js_files(filename):
    return static_file(filename, root='static/js')


@route('/images/<filename:re:.*\.jpg>')
def images(filename):
    return static_file(filename, root='static/images')


def main():
    run(host='localhost', port=7000, debug=True, reloader=True)


if __name__ == '__main__':
    main()
