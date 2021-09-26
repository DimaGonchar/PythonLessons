import sqlite3
import requests
import json
from datetime import datetime

connectToDatabase=sqlite3.connect(r'C:/Users/serge/source/repos/PythonLessons/chackingCurrency/currencies.sqlite3')

while True:
 resp=requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
 listRates=json.loads(resp.text)
 dump=json.dumps(listRates)

 cur=connectToDatabase.cursor()

 jsonData={"day":datetime.now().date().day,"month":datetime.now().date().month,"year":datetime.now().date().year}
 d=json.dumps(jsonData)
 print(type(d))
 cur.execute(f"INSERT INTO currencies VALUES(?,?)", (d,dump))  #{str(datetime.now().date())}', '{ccy}', '{currency}', '{buy}','{sale}'
 connectToDatabase.commit()

 res=cur.execute("SELECT * FROM currencies")
 dataFormDatabase=cur.fetchall()

 for tuple in dataFormDatabase:
   data, carrancy=tuple 
   res=json.loads(carrancy)
   resData=json.loads(data)
   for i in res:
     print(resData['day'],'.',resData['month'],'.',resData['year'], i['ccy'],i['base_ccy'],i['buy'],i['sale'])
     
#connectToDatabase.close()


