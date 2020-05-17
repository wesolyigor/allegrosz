import os
import sqlite3

base_dir = os.path.abspath(os.path.dirname(__file__))
base_dir = base_dir.replace('db_conf', 'allegrosz')
path = os.path.join(base_dir, 'db', 'allegrosz.db')

# TODO find in os how to traverse file's structure
conn = sqlite3.connect(path)
c = conn.cursor()


def show_items():
    items = c.execute('''SELECT
        i.id, i.title, i.description, i.price, i.image, c.name, c.id, s.name, s.id
        FROM
        items AS i
        INNER JOIN categories AS c ON i.category_id = c.id
        INNER JOIN subcategories AS s ON i.subcategory_id = s.id
    ''')

    print('ITEMS')
    print(f"{'#' * 20}")
    for row in items:
        print(f"id: {row[0]}")
        print(f"title: {row[1]}")
        print(f"description: {row[2]}")
        print(f"price: {row[3]}")
        print(f"category name: {row[5]}")
        print(f"subcategory name: {row[6]}")
        print(f"image: {row[7]}")

    conn.close()

#todo write 3 funkcje
def show_categories():
    categories = c.execute('''SELECT
        ''')


def show_subcategories():
    pass


def show_comments():
    pass

#todo jak odpale show tables jako script w terminalu to ma mnie zapytać, ktora tabele chce zobaczyc a nastepnie ta jedna wyswietlic