import sqlite3
def create_table():

    con = sqlite3.connect("finance.db") 
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS finance(id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, amount REAL, category TEXT, description TEXT)")

    con.commit()
    con.close()

def insert_expenses(date, amount, category, description):
    con = sqlite3.connect("finance.db") 
    cur = con.cursor()

    sql = ''' INSERT INTO finance(date, amount, category, description)
              VALUES(?,?,?,?) '''
    
    cur.execute(sql, (date, amount, category, description))
    con.commit()
    con.close()