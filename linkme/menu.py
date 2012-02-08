### MENU ### 


import sqlite3

dbfile = sqlite3.connect('') 

dbcurs = dbfile.cursor()

def table():
	table = dbcurs.execute('''CREATE TABLE "table name"
	(id INTEGER PRIMARY KEY, name TEXT, link TEXT)''')

def main():
	table()
	menu()
	insertdb()
	getdb()
	
def menu():
	print('Welcome to LinkMe!')
	print('Here are your options: ')
	option = raw_input('Do you want to put stuff into the database? (enter i or I) OR read what from it? (enter r or R)?: ')
	if option == 'i':
		insertdb()
	elif option == 'r':
		getdb()

def insertdb():
	name = raw_input('Enter your name or initials: ')
	link = raw_input('Enter the link you want to store in the database: ')
	dbcurs.execute('''INSERT INTO "table name" (name, link) VALUES (?,?)''',(name, link))
	dbfile.commit()
	menu()


def getdb():
	dbcurs.execute('SELECT * FROM "table name" ORDER BY id ASC, name LIMIT 25')

	for i in dbcurs:
		print '\n'
		for j in i:
			print j
				
	dbfile.commit()
	menu()

main()

