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


user_id = "100027991697049"

user_id_1 = '"'+user_id+'"'
r=requests.get('http://10.17.2.210:5984/report/_design/find_user_report/_view/find_user_report_V1?key='+user_id_1)
data_stage=r.text
data_stage=r.json()
total_rows_=data_stage['offset']


print(total_rows_)