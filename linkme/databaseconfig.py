### DATABASE CONFIGURATION ###


import sqlite3

dbfile = sqlite3.connect('') 

dbcurs = dbfile.cursor()

def table():
	dbcurs.execute('''CREATE TABLE "table name"
	(id INTEGER PRIMARY KEY, name TEXT, link TEXT)''')

def insertdb(name, link):
	queryCurs.execute('''INSERT INTO "table name" (name, link)
	VALUES (?,?)''',(name, link))
	dbfile.commit()
	dbfile.close()

def readdb(LIMIT):
	dbcurs.execute('SELECT * FROM "table name" ORDER BY id DESC, name LIMIT')
	labels = ['ID', 'name', 'link']
	t=0
	
	for i in dbcurs:
		print '\n'
		for j in i:
			print lables[t]
			print j
			if t < 10: t+=1
			else: t = 0 
	dbfile.commit()
	dbfile.close()
			
			
			
