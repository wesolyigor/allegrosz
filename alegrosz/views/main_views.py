from flask import Blueprint, render_template, send_from_directory, request

from alegrosz.db import get_db
from alegrosz.forms.filter_forms import FilterForm
from alegrosz.helpers.helpers_images import uploads_path
from werkzeug.utils import escape

main_bp = Blueprint('main', __name__, url_prefix="/")


@main_bp.route('/')
def index():
    conn = get_db()
    c = conn.cursor()

    form = FilterForm(request.args, meta={"csrf": False})

    c.execute("SELECT id, name FROM categories")
    categories = c.fetchall()
    categories.insert(0, (0, "---"))
    form.category.choices = categories

    c.execute("SELECT id, name FROM subcategories")
    subcategories = c.fetchall()
    subcategories.insert(0, (0, "---"))
    form.subcategory.choices = subcategories

    query = """SELECT
        i.id, i.title, i.description, i.price, i.image, c.name, s.name
        FROM
        items AS i
        INNER JOIN  categories AS c ON i.category_id = c.id
        INNER JOIN subcategories AS s ON i.subcategory_id = s.id
    """

    if form.validate():
        filter_queries = []
        paramiters = []

        if form.title.data.strip():
            filter_queries.append("i.title LIKE ?")
            paramiters.append(f"%{escape(form.title.data)}%")

        if form.category.data:
            filter_queries.append("i.category_id = ?")
            paramiters.append(form.category.data)

        if form.subcategory.data:
            filter_queries.append("i.subcategory_id = ?")
            paramiters.append(form.subcategory.data)

        if filter_queries:
            query += " WHERE "
            query += " AND ".join(filter_queries)

        if form.price.data:
            if form.price.data == 1:
                query += " ORDER BY i.price DESC "
            else:
                query += " ORDER BY i.price "
        else:
            query += " ORDER BY i.id DESC "

        items_from_db = c.execute(query, tuple(paramiters))

    else:
        items_from_db = c.execute(query + " ORDER BY i.id DESC ")

    items = []
    for row in items_from_db:
        item = {
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "price": row[3],
            "image": row[4],
            "category": row[5],
            "subcategory": row[6]
        }
        items.append(item)

    return render_template('index.html', items=items, form=form)


@main_bp.errorhandler(403)
def not_found(exception):
    print("1")
    return 'access denied'


@main_bp.errorhandler(403)
def not_found(exception):
    print("1")
    return 'not found'


@main_bp.errorhandler(500)
def internal(exception):
    return 'internal error'


@main_bp.route("/uploads/<filename>")
def uploads(filename):
    return send_from_directory(uploads_path, filename)
