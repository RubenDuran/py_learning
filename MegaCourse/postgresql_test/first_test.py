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

print "\nShow me the databases:\n"
for row in rows:
    print "   ", row[0]

# We create a test table namely Cars. Use the below code to drop the Cars
# table if it already exists, then create the table, and insert some data.

cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute(
    "CREATE TABLE Cars(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")

cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")

conn.commit()

# Now you can run a query to select data from the newly created data and
# print out the result set.

cur.execute("""SELECT * from Cars""")
rows = cur.fetchall()

print "\nShow me the databases:\n"
pprint.pprint(rows)

conn.close()
