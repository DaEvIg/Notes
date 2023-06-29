from connection import *

class Model(Connection):
    def __init__(self):
        super().__init__()
    def create(self):
        try:
            con = self.connect()
            cur = self.con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS User(id INTEGER PRIMARY KEY AUTOINCREMENT,"
                        "login TEXT, password TEXT, name TEXT, e_mail TEXT);")
            cur.execute("CREATE TABLE IF NOT EXISTS Note(id INTEGER PRIMARY KEY AUTOINCREMENT,"
                        "title TEXT, content TEXT, date_of_creation TEXT, user_id INTEGER,"
                        "is_deleted BLOB, FOREIGN KEY (user_id) REFERENCES User(id));")
            con.commit()
            print("таблица успешно создана")
        except sqlite3.Error as err:
            print(f"не удалось создать таблицу {err}")
        finally:
            self.con.close()
    def read(self):
        try:
            con = self.connect()
            cur = self.con.cursor()
            cur.execute("SELECT name FROM User UNION SELECT title FROM Note")
            return cur.fetchall()
        except sqlite3.Error as err:
            print(f"не удалось сделать выборку {err}")
        finally:
            self.con.close()
    def update(self, args1, args2):
        try:
            con = self.connect()
            cur = self.con.cursor()
            cur.execute("INSERT INTO User(login, password, name, e_mail) VALUES(?,?,?,?)", args1)
            cur.execute("INSERT INTO Note(title, content, date_of_creation, is_deleted) VALUES(?,?,?,?)", args2)
            con.commit()
        except sqlite3.Error as err:
            print(f"не удалось внести изменение в таблицу {err}")
        finally:
            self.con.close()
    def delete(self, args1, args2):
        try:
            con = self.connect()
            cur = self.con.cursor()
            cur.execute("DELETE FROM User WHERE name = (?)", args1)
            cur.execute("DELETE FROM Note WHERE title = (?)", args2)
            con.commit()
        except sqlite3.Error as err:
            print(f"не удалось удалить данные таблицы{err}")
        finally:
            self.con.close()


# Model test create
x = Model()
x.create()

# Model test read
# y = Model()
# print(y.read())

# Model test update
# z = Model()
# args1 = ["daevig", "9876", "Danil", "d@mail.ru"]
# args2 = ["first note", "This is our first note!", "29.06.2023", "False"]
# z.update(args1, args2)

# Model test delete
# p = Model()
# args1 = ["Danil"]
# args2 = ["first note"]
# p.delete(args1, args2)