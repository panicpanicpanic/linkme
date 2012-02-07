### MENU ### 


import sqlite3

dbfile = sqlite3.connect('')

dbcurs = dbfile.cursor()


def main():
	menu()
	insert()
	insertdb()
	read()
	getdb()
	
	
def menu():
	print('Welcome to LinkMe!')
	print('Here are your options: ')
	print('\n')
	option = raw_input('Do you want to put stuff into the database? (enter i or I) OR read what from it? (enter r or R)?: ')


def insert(option):
	if option == 'i' or 'I':
		insertdb()
	else:
		print('Confused? Here is the menu again:')
		menu()	
		
def insertdb():
		name = raw_input('Enter your name or initials: ')
		link = raw_input('Enter the link you want to store in the database: ')
		queryCurs.execute('''INSERT INTO "table name" (name, link)		VALUES (?,?)''',(name, link))
		dbfile.commit()
		dbfile.close()
		menu()


def read(option):
	if option == 'r' or 'R':
		getdb()
	else:
		print('Confused? Here is the menu again:')
		menu()

def getdb():
		dbcurs.execute('SELECT * FROM "table name" ORDER BY id DESC, name LIMIT 10')
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
		menu()

menu()
	
