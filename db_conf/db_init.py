import os
import sqlite3

base_dir = os.path.abspath(os.path.dirname(__file__))
base_dir = base_dir.replace('db_conf', 'allegrosz')
path = os.path.join(base_dir, 'db', 'allegrosz.db')

# TODO find in os how to traverse file's structure
print(path)

conn = sqlite3.connect(path)
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS items')
c.execute('DROP TABLE IF EXISTS categories')
c.execute('DROP TABLE IF EXISTS subcategories')
c.execute('DROP TABLE IF EXISTS comments')

c.execute('''CREATE TABLE categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT 
)''')

c.execute('''CREATE TABLE subcategories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category_id INTEGER,
    FOREIGN KEY(category_id) REFERENCES categories(id) 
)''')

c.execute('''CREATE TABLE items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    price REAL,
    image TEXT,
    category_id INTEGER,
    subcategory_id INTEGER,
    FOREIGN KEY(category_id) REFERENCES categories(id) 
    FOREIGN KEY(subcategory_id) REFERENCES subcategories(id) 
)''')

c.execute('''CREATE TABLE comments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT,
    item_id INTEGER,
    FOREIGN KEY(item_id) REFERENCES items(id) 
)''')

categories = [('books',), ('alcohol',), ('music',)]
c.executemany('INSERT INTO categories (name) VALUES (?)', categories)

subcategories = [
    ('reportage', 1),
    ('history', 1),
    ('sci-fy', 1),
    ('whiskey', 2),
    ('wine', 2),
    ('beer', 2),
    ('jazz', 3),
    ('metal', 3),
]
c.executemany('INSERT INTO subcategories (name, category_id) VALUES (?, ?)', subcategories)

items = [
    ('Nie ma', 'Mariusz Szczygieł', 25.99, "", 1, 1),
    ('The Apostasy', 'Behemoth', 29.99, "", 3, 8),
    ('Johny Walker', 'Polmos USA', 34.99, "", 2, 4),
    ('Heban', 'Ryszard Kapuściński', 21.90, "", 1, 1)

]
c.executemany(
    'INSERT INTO items (title, description, price, image, category_id, subcategory_id) VALUES (?, ?, ?, ?, ?, ?)',
    items)

comments = [
    ('zajebista książka', 1),
    ('no fajny, fajny zakup', 2),
    ('stracone pieniądze', 3)
]
c.executemany(
    'INSERT INTO comments (content, item_id) VALUES (?, ?)',
    comments)

conn.commit()
conn.close()

print('Database is created and initialized')
