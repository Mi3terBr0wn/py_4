import cgi
import cgitb
import html

from db import add_genre

cgitb.enable()

form = cgi.FieldStorage()

genre_name = html.escape(form.getvalue('field-genrename'))

add_genre(name=genre_name)

print("Content-type: text/html")
print(f'''
        <!DOCTYPE html>
        <html lang="ru">
            <head>
                <title>База данных</title>
                <meta charset="UTF-8">
            </head>
            <body>
                <h1> Жанр {genre_name} добавлен </h1><br>
                <a href="../templates/index.html">Вернуться на главную страницу</a><br>
            </body>
        </html>
''')
