import sqlite3
import os

db_abs_path = os.path.dirname(os.path.realpath(__file__))
db_name = 'alegrosz.db'

db_path = os.path.join(db_abs_path, db_name)
conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS items')
c.execute('DROP TABLE IF EXISTS categories')
c.execute('DROP TABLE IF EXISTS subcategories')
c.execute('DROP TABLE IF EXISTS comments')

c.execute("""CREATE TABLE categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)""")

c.execute("""CREATE TABLE subcategories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category_id INTEGER,
    FOREIGN KEY(category_id) REFERENCES categories(id)
)""")

c.execute("""CREATE TABLE items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    price REAL,
    image TEXT,
    category_id INTEGER,
    subcategory_id INTEGER,
    FOREIGN KEY(category_id) REFERENCES categories(id),
    FOREIGN KEY(subcategory_id) REFERENCES subcategories(id)
)""")

c.execute("""CREATE TABLE comments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT,
    item_id INTEGER,
    FOREIGN KEY(item_id) REFERENCES items(id)
)""")

categories = [("Food",), ("Technology",), ("Animals",)]

c.executemany("INSERT INTO categories (name) VALUES (?)", categories)

subcategories = [("Fruits", 1),
                 ("Dairy products", 1),
                 ("Meat", 1),
                 ("Phones", 2),
                 ("TVs", 2),
                 ("Household goods", 2),
                 ("Eatable", 3),
                 ("Non eatable", 3),
                 ("Pets", 3)]

c.executemany("INSERT INTO subcategories (name, category_id) VALUES (?, ?)", subcategories)

items = [
    ("Apple", "Red, eatable.", 3.99, "", 1, 1),
    ("Pig", "Fully eatable.", 29.99, "", 3, 7),
    ("iPhone SE", "New old phone for too much.", 1700, "", 2, 4),
    ("Air conditioner", "Necessary in home office", 4999, "", 2, 6),
]

c.executemany(
    "INSERT INTO items (title, description, price, image, category_id, subcategory_id) VALUES (?, ?, ?, ?, ?, ?)",
    items)

conn.commit()
conn.close()

print("DB has been created and initialized")

