from flask import Flask
from redis import Redis, RedisError
import socket


app = Flask(__name__)
redis = Redis(host="redis")


@app.route("/")
def hello():
    try:
        visits = redis.incr('counter')
    except RedisError:
        visits = "<i>counter disabled. Cannot connect to Redis.</i>"

    html = "<h3>Hola Openwebinars!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}<br/>" \
           "<br/>"

    return html.format(hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
