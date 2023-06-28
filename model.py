from connection import *

class Model(Connection):
    def __init__(self):
        super().__init__()
    def create(self, *args):
        try:
            con = self.connect()
            cur = self.con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS User(login, password, name, e_mail)")
            cur.execute("INSERT INTO User(login, password, name, e_mail) VALUES(?,?,?,?)", *args)
            con.commit()
            print("таблица успешно создана")
        except sqlite3.Error as err:
            print(f"не удалось создать таблицу {err}")
    def read(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass

# Model test
# x = Model()
# args = ["daevig", "12345", "Danil", "d@mail.ru"]
# x.create(args)