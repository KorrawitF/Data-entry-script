import mysql.connector
import os

mydb = mysql.connector.connect(
    host="hostname",
    user = "user",
    password = "password",
    database = "database"
)
mycursor = mydb.cursor()

sql = "SELECT field1, field2, file_name FROM table"

path = 'path/to/drive'

mycursor.execute(sql)
results = mycursor.fetchall()
for result in results:
    originalPath = os.path.join(path, result[0], result[2])
    newPath = os.path.join(path, result[0], result[1])
    try: 
        os.rename(originalPath, newPath)
        print(f"file: {originalPath} -> {newPath}")
    except:
        print("File doesn't exist")
mycursor.close()
mydb.close()

# for file in *; do mv "$file" "${file// /}"; #done remove space from name
# pdftk $(ls -v *.pdf) cat output file.pdf #merge pdf