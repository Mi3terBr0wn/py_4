import cgi
import cgitb
import html

from db import add_author

cgitb.enable()

form = cgi.FieldStorage()

author_name = html.escape(form.getvalue('field-authorname'))

add_author(name=author_name)

print("Content-type: text/html")
print(f'''
        <!DOCTYPE html>
        <html lang="ru">
            <head>
                <title>База данных</title>
                <meta charset="UTF-8">
            </head>
            <body>
                <h1> Автор {author_name} успешно добавлен </h1><br>
                <a href="../templates/index.html">Вернуться на главную страницу</a><br>
            </body>
        </html>
''')
