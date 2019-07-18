import sqlite3


conn = sqlite3.connect("test_database.db")
cur = conn.cursor()

print("Hello , Chuck!")

def create():
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INT, title TEXT, year INT)")


def passive_insert():
    cur.execute("INSERT INTO books VALUES(1, 'Financier', 1991)")
    conn.commit()
    
def active_insert(ids, title, year):
    cur.execute("INSERT INTO books VALUES(%i, '%s', %i)"%(ids, title, year))
    conn.commit()
    



create()

for i in range(3,10):
    active_insert(i, "Homo Deus", 1992)


def selector():
    cur.execute("SELECT year, title FROM books WHERE id > 3")
    for temp in cur.fetchall():
        print(temp)

selector()


