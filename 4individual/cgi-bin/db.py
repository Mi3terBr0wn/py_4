import sqlite3
from typing import Dict, List

def sqlite_connection(func):
    def wrapper(*args, **kwargs):
        with sqlite3.connect('db.db') as con:
            kwargs['con'] = con
            res = func(*args, **kwargs)
            con.commit()
        return res
    return wrapper


@sqlite_connection
def init_db(con: sqlite3.Connection):
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS GENRES (
            GENRE_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            GENRE_NAME TEXT
        );""")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS AUTHORS (
            AUTHOR_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            AUTHOR_NAME TEXT
        );""")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS BOOKS (
            BOOK_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            BOOK_NAME TEXT,
            AUTHOR_ID INTEGER,
            GENRE_ID INTEGER,
            FOREIGN KEY (AUTHOR_ID) REFERENCES AUTHORS(AUTHOR_ID),
            FOREIGN KEY (GENRE_ID) REFERENCES GENRES(GENRE_ID)
        );""")
    cur.execute("INSERT INTO GENRES (GENRE_NAME) VALUES ('Комедия');")
    cur.execute("INSERT INTO GENRES (GENRE_NAME) VALUES ('Трагедия');")
    cur.execute("INSERT INTO GENRES (GENRE_NAME) VALUES ('Драма');")
    cur.execute("INSERT INTO AUTHORS (AUTHOR_NAME) VALUES ('Чехов А.П.');")
    cur.execute("INSERT INTO AUTHORS (AUTHOR_NAME) VALUES ('Толстой Л.Н.');")

@sqlite_connection
def get_all_books(con: sqlite3.Connection) -> List:
    cur = con.cursor()
    cur.execute('''
        SELECT B.BOOK_NAME, A.AUTHOR_NAME, G.GENRE_NAME FROM BOOKS B
        LEFT OUTER JOIN AUTHORS A ON B.AUTHOR_ID = A.AUTHOR_ID
        LEFT OUTER JOIN GENRES G ON B.GENRE_ID = G.GENRE_ID;
    ''')
    # cur.execute('select * from books;')
    return cur.fetchall()


@sqlite_connection
def get_all_genres(con: sqlite3.Connection) -> List:
    cur = con.cursor()
    cur.execute('''
            SELECT * FROM GENRES;
        ''')
    return cur.fetchall()


@sqlite_connection
def get_all_authors(con: sqlite3.Connection) -> List:
    cur = con.cursor()
    cur.execute('''
            SELECT * FROM AUTHORS;
        ''')
    return cur.fetchall()


@sqlite_connection
def add_genre(con: sqlite3.Connection, name: str):
    cur = con.cursor()
    cur.execute('''
        INSERT INTO GENRES (GENRE_NAME) VALUES (?);
    ''', (name,))


@sqlite_connection
def add_author(con: sqlite3.Connection, name: str):
    cur = con.cursor()
    cur.execute('''
        INSERT INTO AUTHORS (AUTHOR_NAME) VALUES (?);
    ''', (name,))


@sqlite_connection
def add_book(con: sqlite3.Connection, book_name: str, author_id: int, genre_id: int):
    cur = con.cursor()
    cur.execute('''
        INSERT INTO BOOKS (BOOK_NAME, AUTHOR_ID, GENRE_ID) VALUES (?, ?, ?);
    ''', (book_name, author_id, genre_id))


if __name__ == '__main__':
    init_db()
