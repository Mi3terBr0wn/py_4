import sqlite3
import cgitb

from adapter import export_to_xml
from db import sqlite_connection

PATH = '../books.xml'

cgitb.enable()

@sqlite_connection
def sql_to_xml(con: sqlite3.Connection):
    cur = con.cursor()
    cur.execute("select * from BOOKS;")
    rows = cur.fetchall()
    export_to_xml(rows, PATH)


sql_to_xml()
print("Content-type: text/html")
print(f'''
            <!DOCTYPE html>
            <html lang="ru">
                <head>
                    <title>База данных</title>
                    <meta charset="UTF-8">
                </head>
                <body>
                <h1>Экспорт базы данных в xml файл выполнен</h1><br>
                <a class="btn btn-success" href="../templates/index.html">Вернуться на главную</a><br>
        </body>
        </html>

    ''')