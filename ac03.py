import sqlite3

conn = sqlite3.connect('ACdevops03.db')
c = conn.cursor()
c.execute('''CREATE TABLE ACdevops03
             (id Tnteger Primary Key,
              nome Text Not Null, 
              email Text)''')