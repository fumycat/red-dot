import os
from bottle import route, run, template, static_file
from text import generate_main_container


@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')


@route("/")
def hello_world():
    return template('templates/index.html')


@route('/ajax/<to>', method='POST')
def ajax(to):
    return generate_main_container(int(to))


if __name__ == '__main__':
    # run(host='localhost', port=8080, reloader=True)
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
