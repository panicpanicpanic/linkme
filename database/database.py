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

# This execution is creating the table in the database you just made. It's also creating placeholders for the input values.

# "table name" = when you're ready to pick a table name, enter it! (remove quotes)
# 'id' = each entry will be given an id number. This is to keep track of all of the inputs, which auto-increments. You should leave this one alone!
# 'name' = this is meant for multiple people who are sharing, like on a team. 
# 'link' = this is where you would store your links. 
# You can edit this however you like: adding/deleting columns.

table()