import sqlite3
conn = sqlite3.connect (':memory:')
c = conn.cursor()

c.execute('''CREATE TABLE ACdevops03ex2
             (id integer primary key,
              nome text not null, 
              email text)''')

c.execute("INSERT INTO ACdevops03ex2 VALUES (1,'Guilherme Nascimento','guilherme.rodrigues@aluno.faculdadeimpacta.com.br')")
c.execute("INSERT INTO ACdevops03ex2 VALUES (2,'Guilherme Rodrigues','guilherme.rodrigues@')")

for row in c.execute('SELECT * FROM ACdevops03ex2'):
        print(row)