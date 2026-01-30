import sqlite3
def create_table():

    con = sqlite3.connect("finance.db") 
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS finance(id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, amount REAL, category TEXT, description TEXT)")

    con.commit()
    con.close()

