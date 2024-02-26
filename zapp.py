import requests
import json


def get_data():
    URL = 'http://127.0.0.1:8000/em_info'
    r = requests.get(url=URL)
    data = r.json()
    print(data)
get_data()

def create_data():
    URL = "http://127.0.0.1:8000/em_create/"
    data = {
        'em_name':'Hood',
        'em_email':'robhin@h.com',
        'em_phn':9857
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL,data = json_data)
    p = r.json()
    print(p)

def put_data():
    URL = "http://127.0.0.1:8000/put_em/"
    data = {
        'id':10,
        'em_name':'Robin Hood',
        'em_phn':666
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL,data = json_data)
    p = r.json()
    print(p)



def delete_data(id):
    URL = "http://127.0.0.1:8000/dlt_em/"
    data = {'id':id }
    json_data = json.dumps(data)
    r = requests.delete(url=URL,data = json_data)
    p = r.json()
    print(p)
# delete_data(8)