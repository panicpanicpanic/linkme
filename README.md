# Introduction:

This is a small Python program that is designed to help manage links. The program stores the links into a SQLite database (stored and shared on a DropBox folder-for sharing with others/remote connection).

## Configuration Instructions:

1. Setup the database you want to use:
	* dbfile = sqlite3.connect('') Enter the location and file name for the database you are going to use. Here's an example: '/Users/Angel/Desktop/tdd.db' (make sure it ends in '.db'!)
	* Everywhere there's a "table name" enter a table name that you want to use. Here's an example: links (remove the quotes). Make sure you apply this in the 'table', 'insertdb', and 'getdb' functions where this is a "table name" listed. 
	* Once you run the file once, the table will be created. If you run the file again, you should get an error about the table already existed. Don't freak out- That just means it worked! To get rid of the error, just comment out (put a #) the def table function and it's contents. Also, comment out table() in the main function. It should look like this:

'# def table():
	# table = dbcurs.execute('''CREATE TABLE "table name"
	# (id INTEGER PRIMARY KEY, name TEXT, link TEXT)''')

def main():
	# table()'

2. LINK AWAY!

## Motivations: 
I designed this program because I was becoming overwhelmed with the amount of data I would come across online. Between sending emails to friends, bookmarking, and posting to social networking sites, I figured there had to be a better way to manage my links. Although this technology already exist, I wanted to build something on my own (nonconformist). I also wanted to exercise both my Python and SQL skills. 

One of the reasons why it took so long for me to finish the program was because I kept finding ways of improving my code. I went from using a .txt file to using a SQLite database. I went from 5 python files to just one. Although the program is not necessarily finished, I am proud of what I did with it…it's the best I could do with the skills I currently have. I hope to eventually turn it to an actually functional web app, maybe in rails! 