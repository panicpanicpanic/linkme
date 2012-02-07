### RUN FIRST ###


import sqlite3

dbfile = sqlite3.connect('') 

dbcurs = dbfile.cursor()

def table():
	dbcurs.execute('''CREATE TABLE "table name"
	(id INTEGER PRIMARY KEY, name TEXT, link TEXT)''')

