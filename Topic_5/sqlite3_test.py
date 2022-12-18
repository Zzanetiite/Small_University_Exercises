import sqlite3

db = sqlite3.connect('customers.db')

cur = db.cursor()

cur.execute('SELECT FirstName, Surname, Postcode   \
             FROM customers                        \
             ORDER BY surname;')

for row in cur.fetchall():
    print("{0[0]:<30s} {0[1]:<30s}".format(row))

db.close()
