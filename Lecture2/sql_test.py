import sqlite3

conn = sqlite3.connect("test_base.db")
cur = conn.cursor()




def create():
    cur.execute("CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, year INT) ")

def inserter():
    cur.execute("INSERT INTO books VALUES('The Lord of the Kek','Vlasov Evgen',1927)")
    conn.commit()



def dynamic_inserter(title, name, year):
    cur.execute("INSERT INTO books VALUES('%s','%s',%i)"%(title, name, year))
    conn.commit()

create()
#inserter()

def selector():
    cur.execute("SELECT title FROM books WHERE year >= 2082")
    for i in cur.fetchall():
        print(i)

def sum_selector():
    cur.execute("SELECT year (SELECT * SUM(year) FROM books) total FROM books ")

selector()
sum_selector()