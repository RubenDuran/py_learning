import psycopg2
import pprint

try:
    conn = psycopg2.connect(
        #fake pw
        "dbname='learning' user='postgres' host='localhost' password='PW'")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()
cur.execute('''SELECT datname from pg_database''')
rows = cur.fetchall()


cur.execute(
    "CREATE TABLE Cars(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")
cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
