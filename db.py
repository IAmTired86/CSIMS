import sqlite3
class clothes_database:
    def __init__(self, db):
        self.conn = sqlite3.connect('CSIMS.db')
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS clothes (id INTEGER PRIMARY KEY, name text, color text, size text, stock integer, price integer)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM clothes")
        rows = self.cur.fetchall()
        return rows
    


    def insert(self, name, color, size, stock, price):
        self.cur.execute("INSERT INTO clothes VALUES (NULL, ?, ?, ?, ?, ?)",
                         (name, color, size, stock, price))
        self.conn.commit()


    def remove(self, id):
        self.cur.execute("DELETE FROM clothes WHERE id=?", (id,))
        self.conn.commit()
 

    def update(self, id, name, color, size, stock, price):
        self.cur.execute("UPDATE clothes SET name = ?, color = ?, size = ?, stock = ?, price = ? WHERE id = ?",
                         (name, color, size, stock, price, id))
        self.conn.commit()
  
    def __del__(self):
        self.conn.close()


class employees_database:
    def __init__(self, db):
        self.conn = sqlite3.connect('CSIMS.db')
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name text, age integer, email text, address text, phone text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM employees")
        rows = self.cur.fetchall()
        return rows
    


    def insert(self, name, age, email, address, phone):
        self.cur.execute("INSERT INTO employees VALUES (NULL, ?, ?, ?, ?, ?)",
                         (name, age, email, address, phone))
        self.conn.commit()


    def remove(self, id):
        self.cur.execute("DELETE FROM employees WHERE id=?", (id,))
        self.conn.commit()
 

    def update(self, id, name, age, email, address, phone):
        self.cur.execute("UPDATE employees SET name = ?, age = ?, email = ?, address = ?, phone = ? WHERE id = ?",
                         (name, age, email, address, phone, id))
        self.conn.commit()
  
    def __del__(self):
        self.conn.close()