### INSERT SQL SCRIPT ###


import sqlite3

dbfile = sqlite3.connect('') 
# Enter the location of the database file (should be in 'database.py' file)

dbcurs = dbfile.cursor()
	
def insert(name, link):
	queryCurs.execute('''INSERT INTO "table name" (name, link)
	VALUES (?,?)''',(name, link))

# Change the "table name" to the name mentioned in database.py. If you added any new variables, be sure to pass them along through the 'insert' function. If they aren't mentioned, they won't be included.

	
def main():
	
	insert(name, link)
	
	createDb.commit()
	
main()
