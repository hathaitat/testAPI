import dbchat
import requests
import check_user_permission
import json
import report_daily
from flask import Flask, request, jsonify, render_template
#from flask_sslify import SSLify
web_hook_url="https://graph.facebook.com/v2.6/me/messages?access_token=DQVJzemlHdVlSRGFjcDhCWVFpcWo2VzE3R3R2M3M3VWQzX1drLWJpcTVqZA19IWVpCaFBYSEVKbW5yeHFMdVMzSnp1QjFobWktcDJYX1M1a3RIeHplWktweEhBczdCaGVkLTVFQ2RFdnp1MzhRMFNLUjRXY29tZA1N1TjNoS3lWT0VCZAU9xVmhVekxPZAmJQUDNMdkdwUFNoeHlKRW1xT2xFVVBrZATRxWTZAtOVNxd0ZAIZAGxFZAS12ekR3SkFLM3VlaDlhRk52cjVn"
hd = {
    "content-type":"application/json"
}

app = Flask(__name__)
#sslify = SSLify(app)


#input parameter 
@app.route('/', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        #################################### check user id ############################################
        
        VERIFY_TOKEN = "ga75HpoblY9qBtOKo2m8QXauNvBoKQzt" # Key for Verify Token
        hubverify = request.args.get('hub.verify_token') # Get Verify Key tokem
        user_id = request.args.get('hub.user_id') 
        if hubverify == VERIFY_TOKEN : # Check data verify and mode
           
            user_id_1 = '"'+user_id+'"'
            r=requests.get('http://10.17.2.210:5984/report/_design/find_user_report/_view/find_user_report_V1?key='+user_id_1)
            data_stage=r.text
            data_stage=r.json()
            print(data_stage)
            Netsale_TY = data_stage['rows'][0]['value'][0][0]['Netsale_TY']
            Netsale_LY = data_stage['rows'][0]['value'][0][1]['Netsale_LY']
            
            json_f = {"Netsale_TY":Netsale_TY,"Netsale_LY":Netsale_LY}
            print(json_f)
            file_data ="/opt/app/micro_service/data.json"
            # file_data ="data.json"
            with open(file_data, 'w') as outfile:
                json.dump(json_f, outfile)
                outfile.close
            return render_template('page.html')
        else:
            return "error"

    # elif request.method == 'POST':
    #     data = request.get_json()
    #     user_id = data['user_id']['id']
    #     date = data['parameter']['date']
    #     print(user_id)
    #     permission=check_user_permission.select_data_from_user_permission_table(user_id)
    #     if permission == "user_have_the_permission":
    #         user_id_1 = '"'+user_id+'"'
    #         r=requests.get('http://10.17.2.210:5984/report/_design/find_user_report/_view/find_user_report_V1?key='+user_id_1)
    #         data_stage=r.text
    #         data_stage=r.json()
    #         total_rows_=data_stage['total_rows']
    #         if total_rows_== 0:
    #             #input parameter from dialogflow
    #             ###########################################
    #             #input data to couch DB
                

    #             datareport = report_daily.get_report_daily(date)
    #             print(datareport)
    #             data_json = {"user_id":user_id,"report":datareport}
    #             dbchat.db_insert('report',data_json)
    #             ###########################################
    #         else:
    #             data_id = data_stage['rows'][0]['id']
    #             data_value = data_stage['rows'][0]['value'][1]
    #             _reV=dbchat.db_delete("report",data_id,data_value)

    #             #insert new data
    #             datareport = report_daily.get_report_daily(date)
    #             data_json = {"user_id":user_id,"report":datareport}
    #             dbchat.db_insert('report',data_json)
    #     return jsonify(data_stage)
   
        


@app.route('/return_data', methods=['GET'])
def test():
    if request.method == 'GET':
        file_data ="/opt/app/micro_service/data.json"
        # file_data = "data.json"
        f = open(file_data, 'r')
        s = f.read()
        f.close()
        return s

@app.route('/test', methods=['GET','POST'])
def test1():
    if request.method == 'GET':
        VERIFY_TOKEN = "ga75HpoblY9qBtOKo2m8QXauNvBoKQzt" # Key for Verify Token
        hubverify = request.args.get('hub.verify_token') # Get Verify Key tokem
        user_id = request.args.get('hub.user_id') 
        type_show= request.args.get('hub.type') 
        if hubverify == VERIFY_TOKEN : # Check data verify and mode
           
            user_id_1 = '"'+user_id+'"'
            r=requests.get('http://10.17.2.210:5984/report/_design/find_user_report/_view/find_user_report_V1?key='+user_id_1)
            data_stage=r.text
            data_stage=r.json()
            print(data_stage)
            Netsale_TY = data_stage['rows'][0]['value'][0][0]['Netsale_TY']
            Netsale_LY = data_stage['rows'][0]['value'][0][1]['Netsale_LY']
            
            json_f = {"Netsale_TY":Netsale_TY,"Netsale_LY":Netsale_LY}
            print(json_f)
            file_data ="/opt/app/micro_service/data.json"
            # file_data ="data.json"
            with open(file_data, 'w') as outfile:
                json.dump(json_f, outfile)
                outfile.close
            if type_show == "table":
                return render_template('Table.html')
            elif type_show == "pie":
                return render_template('page.html')
        else:
            return "error"
    
    elif request.method == 'POST':
        data = request.get_json()
        user_id = data['user_id']['id']
        date = data['parameter']['date']
        print(user_id)
        permission=check_user_permission.select_data_from_user_permission_table(user_id)
        if permission == "user_have_the_permission":
            user_id_1 = '"'+user_id+'"'
            r=requests.get('http://10.17.2.210:5984/report/_design/find_user_report/_view/find_user_report_V1?key='+user_id_1)
            data_stage=r.text
            data_stage=r.json()
            N_rows=data_stage['offset']
            if N_rows== 1:
                #input parameter from dialogflow
                ###########################################
                #input data to couch DB
                

                datareport = report_daily.get_report_daily(date)
                print(datareport)
                data_json = {"user_id":user_id,"report":datareport}
                dbchat.db_insert('report',data_json)
                ###########################################
            else:
                data_id = data_stage['rows'][0]['id']
                data_value = data_stage['rows'][0]['value'][1]
                _reV=dbchat.db_delete("report",data_id,data_value)

                #insert new data
                datareport = report_daily.get_report_daily(date)
                data_json = {"user_id":user_id,"report":datareport}
                dbchat.db_insert('report',data_json)
        
        else:
            msg={"recipient":{"id":user_id},"message":{"text":"you don't have permission"}}
            requests.post(web_hook_url, headers=hd, data=json.dumps(msg)) 
        return jsonify(data_stage)
   

@app.route('/wa1', methods=['GET'])
def test_1():
    if request.method == 'GET':
   
        return render_template('test.html')

@app.route('/wa2', methods=['GET'])
def test_2():
    if request.method == 'GET':
   
        return render_template('page.html')


if __name__ == '__main__':
    app.debug = True
    app.run()