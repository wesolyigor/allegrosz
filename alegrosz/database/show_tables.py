# from alegrosz.database.db_init import c
#
#
# def show_items():
#     items = c.execute("""SELECT
#         i.id, i.title, i.description, i.price, i.image, c.name, c.id, s.name, s.id
#         FROM
#         items AS i
#         INNER JOIN categories AS c ON i.category_id = c.id
#         INNER JOIN subcategories  AS s ON i.subcategory_id  = s.id
#     """)
#
#     print("Items:")
#     print(f"{'@' * 30}")
#     for row in items:
#         print(f"id: {row[0]}")
#         print(f"title: {row[1]}")
#         print(f"description: {row[2]}")
#         print(f"price: {row[3]}")
#         print(f"image: {row[4]}")
#         print(f"category_name: {row[5]} {row[6]}")
#         print(f"subcategory_name: {row[7]} {row[8]}")
#
#
# subcategories = c.execute(
#     "SELECT s.id, s.name, c.name, c.id FROM subcategories AS s INNER JOIN categories AS c ON s.category_id = c.id")
