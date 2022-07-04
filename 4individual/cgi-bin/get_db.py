import cgitb

from db import get_all_genres, get_all_authors, get_all_books

cgitb.enable()

print("Content-type: text/html")
print(f'''
        <!DOCTYPE html>
        <html lang="ru">
            <head>
                <title>База данных</title>
                <meta charset="UTF-8">
            </head>
            <body>
                <h1> Жанры </h1>
                <ul>
                        ''')
try:
    for row in get_all_genres():
        print(f'<li>{row}</li>')
    print('''
                    </ul>
                    <h1> Авторы </h1>
                    <ul>''')
except Exception:
    pass
try:
    for row in get_all_authors():
        print(f'<li>{row}</li>')
    print('''
                    </ul>
                    <h1> Книги </h1>
                    <ul>''')
except Exception:
    pass
try:
    for row in get_all_books():
        print(f'<li>{row}</li>')

    print('''

                    </ul>
                <form action="../cgi-bin/sql_to_xml.py">
                    <input type="submit" class="btn btn-primary" value="Сгенерировать отчёт по книге в xml">
                </form>
    ''')
except Exception:
    pass
print('''
                <form action="../cgi-bin/xml_to_sql.py">
                    <input type="submit" value="Создать базу данных из xml">
                </form><br>
                <a href="../templates/index.html">Вернуться на главную</a><br>
            </body>
        </html>
        ''')

