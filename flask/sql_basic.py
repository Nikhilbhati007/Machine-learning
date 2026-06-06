import sqlite3 as sq

conn = sq.connect('data.db')

conn.execute("DROP TABLE IF EXISTS CUSTOMER")

conn.execute('''
CREATE TABLE IF NOT EXISTS CUSTOMER(
    ID   INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE  INT NOT NULL
);
''')

conn.execute("INSERT INTO CUSTOMER (ID,NAME,AGE) VALUES (1,'NIKHIL',21)")
conn.execute("INSERT INTO CUSTOMER (ID,NAME,AGE) VALUES (2,'Lucky',19)")

all_data = conn.execute("SELECT * FROM CUSTOMER")

for row in all_data:
    print(row)

conn.commit()
conn.close()