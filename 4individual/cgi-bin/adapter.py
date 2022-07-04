from typing import List
from xml.dom import minidom as md


def export_to_xml(data: List, path: str):
    str_data = [[str(el) for el in row] for row in data]
    root = md.Document()
    doc = root.createElement('books')
    root.appendChild(doc)
    for row in str_data:
        book_child = root.createElement('book')
        book_child.setAttribute('id', row[0])
        book_child.setAttribute('name', row[1])
        book_child.setAttribute('author_id', row[2])
        book_child.setAttribute('genre_id', row[3])
        doc.appendChild(book_child)
    xml_str = root.toprettyxml()
    with open(path, 'w+') as f:
        f.write(xml_str)


def import_from_xml(path: str):
    with open(path, 'r') as f:
        xml_data = f.read()
    xmlparse = md.parseString(xml_data)
    books = xmlparse.getElementsByTagName('book')
    data = []
    for book in books:
        row = [book.getAttribute('id'),
               book.getAttribute('name'),
               book.getAttribute('author_id'),
               book.getAttribute('genre_id')]
        data.append(row)
    return data

