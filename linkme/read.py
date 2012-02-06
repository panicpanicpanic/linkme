### READ SQL SCRIPT ###


import sqlite3

dbfile = sqlite3.connect('') 
# Enter the location of the database file (should be in 'database.py' file)

dbcurs = dbfile.cursor()
	
def read(lim):
	dbcurs.execute('SELECT * FROM "table name" ORDER BY id DESC, name LIMIT', lim)
	# Make sure you enter the table name you created from the 'database' file.
	for i in dbcurs:
		print '\n'
		for j in i:
			print j

def main():
	read(lim)
	dbfile.close()

main()
