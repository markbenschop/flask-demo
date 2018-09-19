import os
import datetime
import socket
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    message = 'Hello world !'
    hostname = socket.gethostname()
    time = datetime.datetime.now()
    try:
        my_name = os.environ['NAME']
    except KeyError:
        my_name = None

    return render_template('hello.html', message=message, hostname=hostname, time=time , my_name=my_name)


if __name__ == '__main__':

    app.run(host='0.0.0.0')
    # app.run(debug=True, host='0.0.0.0')
