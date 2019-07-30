import requests
import json

hd = {
    "content-type":"application/json"
}

def db_update(db_name,key_name, key_rev):
    
    return "PUT"


def db_insert(db_name,data_in):
    ### Insert data by method POST ###
    rp = requests.post("http://10.17.2.210:5984/" + db_name , headers=hd, data=json.dumps(data_in))
    return rp.status_code

def db_select(db_name, key_name):
    ### Select data by method GET ###
    key_name_="'"+key_name+"'"
    rg = requests.get("http://10.17.2.210:5984/" + db_name + "/" + key_name_)

    return rg.json()

def db_delete(db_name, key_name, key_rev):
    ### Delete data by method DELETE ###
    rd = requests.delete("http://10.17.2.210:5984/" + db_name +"/" + key_name +"?rev=" + key_rev )
    return "DELETE"