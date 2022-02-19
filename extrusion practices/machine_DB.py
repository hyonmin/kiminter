import sqlite3

class no_name_yet:
    def __init__(self):
        self.con = sqlite3.connect('ext.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS rolls(
            RealTime datetime,
            Date text,
            Article text,
            Weight float,
            Machine text,
            product code integer,
            worker ID integer
            modified interger
        )
        """)
    def write():
        return

    def modify():
        return
    
    def read():
        return

    def delete():
        return

    def listArticle():
        return