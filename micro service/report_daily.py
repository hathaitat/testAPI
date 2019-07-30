from flask import Flask, request, jsonify, render_template
import decimal
import json
import pyodbc
import collections

# SELECT [Store_wk],[Storeno],[Netsale_TY] FROM [DBDatawarehouseII].[dbo].[Fact_SaleStore] where SaleDate_TY = '20190417' AND Store_wk ='10'
def get_report_daily(date):
#date from all store
  date = "'"+date+"'"
  dsn = 'sqlserverdatasource'
  user = 'SVC_Chat'
  password = "Pbj'pkd"
  database = 'DBDatawarehouseII'

  con_string = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (dsn, user, password, database)
  # con_string = "DRIVER={SQL Server};SERVER=OFM_BI_PRO\PRD;DATABASE=DBDatawarehouseII;UID=SVC_Chat;PWD=Pbj'pkd"


  cnxn = pyodbc.connect(con_string)
  cursor = cnxn.cursor()
  cursor.execute("""
           SELECT sum([Netsale_TY]) Total_TY,sum([Netsale_LY]) Total_LY FROM [DBDatawarehouseII].[dbo].[Fact_SaleStore] where SaleDate_TY = """ +date
            )
  rows = cursor.fetchall()
  # Convert query to row arrays
  rowarray_list = ['']
  for row in rows:
      t = (row.Total_TY)
      rowarray_list.append(t)
  j_TY = json.dumps(rowarray_list,cls=DecimalEncoder)

  for row in rows:
      t = (row.Total_LY)
      rowarray_list.append(t)
  j_LY = json.dumps(rowarray_list,cls=DecimalEncoder)


  objects_list = []
  for row in rows:
    d = collections.OrderedDict()
    d['Netsale_TY'] = row.Total_TY


    objects_list.append(d)
  j_TY = json.dumps(objects_list,cls=DecimalEncoder)

  objects_list = []
  for row in rows:
    d = collections.OrderedDict()
    d['Netsale_LY'] = row.Total_LY


    objects_list.append(d)
  j_LY = json.dumps(objects_list,cls=DecimalEncoder)

  cnxn.close()
 
  data_report_TY = json.loads(j_TY)
  data_report_TY = data_report_TY[0]

  data_report_LY = json.loads(j_LY)
  data_report_LY = data_report_LY[0]
  
  return data_report_TY,data_report_LY

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)


