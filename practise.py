import json
import sqlite3


with open("practicejson.json", "r") as file:
    json_data = file.read()
    data = json.loads(json_data)

print(data)

conn = sqlite3.connect('text.db')
cursor = conn.cursor()

# Create Employees table if not exists
cursor.execute("CREATE TABLE IF NOT EXISTS Employees (id INTEGER PRIMARY KEY, name TEXT,age INTEGER,department TEXT,company TEXT)")
                   
# Create Address table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS Address (employee_id INTEGER,street TEXT,city TEXT,zipcode INTEGER,FOREIGN KEY (employee_id) REFERENCES Employees(id))''')
                                        

# Insert data into Employees and Address tables
for employee in data.get('employees', []):
    cursor.execute(''' INSERT INTO Employees (name, age, department, company)
                      VALUES (?, ?, ?, ?)''',(employee['name'], employee['age'], employee['department'], data['company']))
    
    employee_id = cursor.lastrowid
    address_data = data.get('address', {})
    cursor.execute('''INSERT INTO Address (employee_id, street, city, zipcode)
                      VALUES (?, ?, ?, ?)''',(employee_id, address_data.get('street', ''), address_data.get('city', ''), address_data.get('zipcode', 0)))
                   
conn.commit()
conn.close()
