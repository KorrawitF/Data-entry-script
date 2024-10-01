import json
import mysql.connector

mydb = mysql.connector.connect(
    host="x.x.x.x",
    user="user",
    password="pass",
    database="db"
)
mycursor = mydb.cursor()

with open('subdis.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

location = list(data)

# print(location[:10])
sql = "INSERT INTO zzzvvvv(Shape_Leng,Shape_Area,ADM3_EN,ADM3_TH,ADM3_PCODE,ADM3_REF,ADM3ALT1EN,ADM3ALT2EN,ADM3ALT1TH,ADM3ALT2TH,ADM2_EN,ADM2_TH,ADM2_PCODE,ADM1_EN,ADM1_TH,ADM1_PCODE,ADM0_EN,ADM0_TH,ADM0_PCODE,date,validOn,coordinates) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

for item in location:
    data = tuple(str(item[field]) if item[field] is not None else '' for field in [
        'Shape_Leng', 'Shape_Area', 'ADM3_EN', 'ADM3_TH', 'ADM3_PCODE', 'ADM3_REF', 'ADM3ALT1EN', 'ADM3ALT2EN', 'ADM3ALT1TH', 
        'ADM3ALT2TH', 'ADM2_EN', 'ADM2_TH', 'ADM2_PCODE', 'ADM1_EN', 'ADM1_TH', 'ADM1_PCODE', 'ADM0_EN','ADM0_TH','ADM0_PCODE','date','validOn','coordinates'
    ])
    mycursor.execute(sql, data)
    mydb.commit()
    print(data)
        
f.close()

