import os
from bottle import route, run, template


@route("/")
def hello_world():
    return "Hello World!"


run(host='localhost', port=8080)
# run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
