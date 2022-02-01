import psycopg2

hostname = 'host'
username = 'user'
password = 'psswd'
database = 'db'
connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
cur = connection.cursor()
cur.execute("""SELECT namefield, image FROM schema.table 
            where = clause
            """)
rows = list()
rows = cur.fetchall()

for row in rows:
    print(row[0])
    with open('/path/'+ row[0],'wb') as f:
        f.write(row[1])