import sqlite3
import pandas as pd
# Creazione database
conn = sqlite3.connect('INSTRUCTOR.db')

cursor_obj = conn.cursor()

# Creazione tabella nel database
cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")

table = """CREATE TABLE IF NOT EXISTS INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2));"""

cursor_obj.execute(table)
print("Table is ready")
# Inserimento dati nella tabella
cursor_obj.execute('''insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')''')
cursor_obj.execute('''insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')''')
query_update='''update INSTRUCTOR set CITY='MOOSETOWN' where FNAME="Rav"'''
cursor_obj.execute(query_update)

# Query

statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)

print("All the data")
output_all = cursor_obj.fetchall()
for row_all in output_all:
    print(row_all)

# Creiamo un dataset con pandas

df = pd.read_sql_query("select * from instructor;", conn)
print(df)
print (df.LNAME[0])

# Chiusura della connessione
conn.close()
