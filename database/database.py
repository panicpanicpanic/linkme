### DATABASE CONFIGURATION ###

# WHEN YOU ARE DONE CONFIGURING THE FILE, RUN IT!# 


import sqlite3

dbfile = sqlite3.connect('') 
# Enter the location and file name you want the database file. Here's an example: '/Users/Angel/Desktop/test.db'. Don't forget the '.db' at the end!

dbcurs = dbfile.cursor()
# The cursor allows you to interact with the database.

def table():
	dbcurs.execute('''CREATE TABLE "table name"
	(id INTEGER PRIMARY KEY, name TEXT, link TEXT)''')

# This execution is creating the table in the database you just made. Change the "table name" to the name you want to use (remove quotes). You can edit this however you like: adding/deleting columns.

def main():
	
	table()
	
	dbfile.commit()
	
main()