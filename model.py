from connection import *

class Model(Connection):
    def __init__(self):
        super().__init__()
    def create(self, *args):
        try:
            con = self.connect()
            cur = self.con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS User(login, password, name, e_mail)")
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
            cur.execute("SELECT name FROM User")
            return cur.fetchall()
        except sqlite3.Error as err:
            print(f"не удалось сделать выборку {err}")
        finally:
            self.con.close()
    def update(self, *args):
        try:
            con = self.connect()
            cur = self.con.cursor()
            cur.execute("INSERT INTO User(login, password, name, e_mail) VALUES(?,?,?,?)", *args)
            con.commit()
        except sqlite3.Error as err:
            print(f"не удалось внести изменение в таблицу {err}")
        finally:
            self.con.close()
    def delete(self, *args):
        try:
            con = self.connect()
            cur = self.con.cursor()
            cur.execute("DELETE FROM User WHERE name = (?)", *args)
            con.commit()
        except sqlite3.Error as err:
            print(f"не удалось удалить данные таблицы{err}")
        finally:
            self.con.close()


# Model test create
# x = Model()
# args = ["daevig", "12345", "Danil", "d@mail.ru"]
# x.create(args)

# Model test read
#y = Model()
#y.read()

# Model test update
#z = Model()
#args = ["qwerty", "54321", "Sergey", "s@gmail.com"]
#z.update(args)

# Model test delete
# p = Model()
# args = ["Danil"]
# p.delete(args)