import os
import datetime
import requests
import json
from creds import url, chat_id

stream = os.popen("docker ps -aq")
ps = stream.read()
containers = ps.split('\n')
del containers[-1]
message = 'Name | Image | Status | Uptime'
for i in containers:
    string = ''
    stream = os.popen(f"docker inspect -f '{{{{json .Name}}}}' {i}")
    name = stream.read()
    name = name[2:-2]
    string = string + name
    stream = os.popen(f"docker inspect -f '{{{{json .Config.Image}}}}' {i}")
    image = stream.read()
    image = image[1:-2]
    string = string + ' | ' + image
    stream = os.popen(f"docker inspect -f '{{{{json .State.Status}}}}' {i}")
    status = stream.read()
    status = status[1:-2]
    string = string + ' | ' + status
    if status == 'running':
        stream = os.popen(f"docker inspect -f '{{{{json .State.StartedAt}}}}' {i}")
        started = stream.read()
        started = started[1:20]
        date_obj = datetime.datetime.fromisoformat(started)
        uptime = datetime.datetime.now() - date_obj
        string = string + ' | ' + str(uptime)
    message = message + "\n" + string

request_body = {'chat_id': chat_id, 'text': message}

requests.get(url, params = request_body)

