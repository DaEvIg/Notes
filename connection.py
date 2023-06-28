import sqlite3
class Connection:
    def __init__(self):
        pass
    def connect(self):
        try:
            self.con = sqlite3.connect("notes.db")
            return self.con
        except sqlite3.Error as err:
            print(f"не удалось подключиться к БД {err}")
            #input()

# test connection
#x = Connection()
#x.connect()
