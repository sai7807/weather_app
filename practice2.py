import json
import sqlite3

with open("practice2.json", "r") as file:
    jsonRead = file.read()
    pythonRead = json.loads(jsonRead)

print(pythonRead)

conn = sqlite3.connect('text.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS personInfo(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,age INTEGER,
               street TEXT, city TEXT, zipcode INTEGER, latitude REAL,longitude REAL,
               type VARCHAR, value TEXT, relationship TEXT,familyname TEXT)''')

#cursor.execute('''ALTER TABLE personInfo ADD COLUMN relationship1 TEXT, familyname1 TEXT''')


    
cursor.execute('''INSERT INTO personInfo (name ,age ,street ,city ,zipcode , latitude ,longitude)
                VALUES(?,?,?,?,?,?,?)''',(pythonRead['name'],pythonRead['age'],pythonRead['address']['street'],
                                                   pythonRead['address']['city'],pythonRead['address']['zipcode'],
                                                    pythonRead['address']['coordinates']['latitude'],pythonRead['address']['coordinates']['longitude'],
                                                    
                                                    ))
                                                    

for contact in pythonRead['contacts']:
    cursor.execute('''INSERT INTO personInfo (type , value) VALUES(?,?)''',(contact['type'],contact['value']))
    
for member in pythonRead['family_members']:
    cursor.execute('''INSERT INTO personInfo (relationship ,familyname) VALUES(?,?)''',(member['relationship'],member['familyname']))

conn.commit()
conn.close()