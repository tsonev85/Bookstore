import sqlite3 as db


class Database:

    def __init__(self):
        self.conn = db.connect('dbfiles/lite.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cursor.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()

    def search(self, title="", author="", year="", isbn=""):
        self.cursor.execute("SELECT * FROM book b "
                       "WHERE b.title=? OR b.author=? OR b.year=? OR b.isbn=?", (title, author, year, isbn))
        rows = self.cursor.fetchall()
        return rows

    def query(self):
        self.cursor.execute("SELECT * FROM book")
        rows = self.cursor.fetchall()
        return rows

    def delete(self, id):
        self.cursor.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# connect()
# insert("Something", "Someone", 1975, 124515)
# print(query())
# delete(2)
# print(search(author="Rosti"))
