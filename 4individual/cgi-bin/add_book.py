import cgi
import cgitb
import html

from db import get_all_genres, get_all_authors, add_book

cgitb.enable()

form = cgi.FieldStorage()
print("Content-type: text/html")
print(f'''
            <!DOCTYPE html>
            <html lang="ru">
                <head>
                    <title>Добавить книгу</title>
                    <meta charset="UTF-8">
                </head>
                <body>
''')
if form:
    book_name = form.getvalue('book_name')
    author = form.getvalue('author')
    genre = form.getvalue('genre')

    add_book(
        book_name=book_name,
        author_id=author,
        genre_id=genre,
    )
    print(f'''<h1>Книга {book_name} добавлена </h1>''')

print('''
                <h1> Добавить книгу </h1>
                <form>
                    <label> Название
                    <input type="text" name="book_name"> 
                    <label> Выбрать автора
                    <select name="author">
                            ''')
for row in get_all_authors():
    print(f'<option value="{row[0]}">{row[1]}</option>')

print('''
                    </select>
                    </label><br>
                    <label> Выбрать жанр 
                    <select name="genre">
                    ''')
for row in get_all_genres():
    print(f'<option value="{row[0]}">{row[1]}</option>')
print('''
                    </select>
                    </label><br>
                    <input type="submit" value="Отправить"></input>
                </form><br>
                <br>
                <a href="../templates/index.html">Вернуться на главную</a><br>
                </body>
            </html>
                            ''')

