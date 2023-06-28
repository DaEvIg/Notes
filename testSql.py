import sqlite3
con = sqlite3.connect("notes.db")
cur = con.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS User(login, password, name, e-mail)")
# cur.execute("CREATE TABLE IF NOT EXISTS Note(title, content, date_of_creation, is_deleted)")
cur.executescript("""
    BEGIN;
    CREATE TABLE IF NOT EXISTS User(login, password, name, e_mail);
    CREATE TABLE IF NOT EXISTS Note(title, content, date_of_creation, is_deleted);
    COMMIT;
""")
#con.commit()
con.close()