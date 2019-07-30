import requests


def select_data_from_user_permission_table(key):
    user_id= key
    key_1= '"'+ user_id +'"'
    r=requests.get('http://10.17.2.210:5984/data-permission/_design/user_permission/_view/user_permission_v1?key='+key_1)
    data_permission=r.text
    data_permission=r.json()
    try :
        user_permission=data_permission['rows']
        if user_permission == []:
            #print("user_don't_have_the_permission")
            return "user_don't_have_the_permission"
        else:
            #print("user_have_the_permission")
            return "user_have_the_permission"
    except:
        print("error from select_data_from_CouchDB")
        return "error from select_data_from_CouchDB"