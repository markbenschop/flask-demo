import os
import datetime
import socket
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    message = 'Hello'
    hostname = socket.gethostname()
    time = datetime.datetime.now()
    try:
        my_name = os.environ['USER']
    except KeyError:
        my_name = 'Unknown'
    try :
        my_var = os.environ['MY_VAR']
    except KeyError:
        my_var = None

    return render_template('hello.html', message=message, hostname=hostname, time=time , my_name=my_name, my_var=my_var)


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    app.run(host='0.0.0.0')

