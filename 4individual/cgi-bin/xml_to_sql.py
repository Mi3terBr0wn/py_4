import cgitb
import sqlite3

from adapter import import_from_xml
from db import init_db, sqlite_connection

PATH = 'books.xml'

cgitb.enable()
init_db()


@sqlite_connection
def xml_to_sql(con: sqlite3.Connection):
    rows = import_from_xml(PATH)
    ins = []
    for row in rows:
        a = []
        for value in row:
            try:
                a.append(int(value))
            except ValueError:
                a.append(value)
        ins.append(a)
    print(ins)
    cur = con.cursor()
    cur.executemany("""
        INSERT INTO BOOKS (BOOK_ID, BOOK_NAME, AUTHOR_ID, GENRE_ID) VALUES (?, ?, ?, ?);
    """, ins)

xml_to_sql()
print("Content-type: text/html")
print(f'''
            <!DOCTYPE html>
            <html lang="ru">
                <head>
                    <title>База данных</title>
                    <meta charset="UTF-8">
                </head>
                <body>
                <h1>Импорт из xml файла в базу данных выполнен</h1><br>
                <a href="../cgi-bin/get_db.py">Вернуться на главную</a><br>
                <a href="../templates/index.html">Вернуться на главную</a><br>
        </body>
        </html>

    ''')