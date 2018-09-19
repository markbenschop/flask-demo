import os
import socket
import datetime

hostname = socket.gethostname()
print(hostname)
time = datetime.datetime.now()
print(time)
my_name = os.environ['USER']
print(my_name)
try :
    my_var = os.environ['MY_VAR']
except KeyError:
    my_var = ''
print(my_var)