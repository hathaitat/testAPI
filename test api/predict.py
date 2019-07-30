from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS



app = Flask(__name__)
# Enable CORS
CORS(app)

@app.route("/predict", methods=["POST"]) #กำหนด url path,การส่ง methods
def predict():
	
	if request.method == "POST":    	
		input_value = request.form["input_value"] #เลือกค่ามาจาก from ที่คีย์เอาไว้
		# response = request.body()
		# input_value = request.urlencoded["input_value"]
		print(input_value)
		# print(response)
		
	return jsonify(  #ตอบค่ากลับไปเป็น JSON ด้วยฟังก์ชั่น jsonify
		prediction=input_value
		# prediction=response


			),201 








# def predict1():
# 	if request.method == "POST":    	
# 		input_value1 = request.body["input_value1"]
# 		# input_value = request.urlencoded["input_value"]
# 		print(input_value1)
		
# 	return jsonify(  #ตอบค่ากลับไปเป็น JSON ด้วยฟังก์ชั่น jsonify
# 		prediction1=input_value1

		
# 	),201 





		
# input_value1 ="Zl4G2mTml9tPkjJ8dUMTEfeUAtMnfVBN3UcG3FstY6K"
# print (input_value1)




# from flask import Flask, request, jsonify
# from flask_restful import Resource, Api, reqparse
# from flask_cors import CORS

# app = Flask(__name__)
# # Enable CORS
# CORS(app)

# @app.route("/predict", methods=["POST"])
# def predict():
# 	result = 0
# 	if request.method == "POST":    		
# 		input_value = request.form["input_value"]
# 		# ประมวลผล
# 		# ...
# 		# ตัวอย่างเช่น รับค่ามา แล้ว คูณ 2
# 		result=input_value * 2
# 		# ###
# 	return jsonify(
# 		prediction=result
# 	),201