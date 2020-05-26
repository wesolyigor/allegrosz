import sqlite3
from flask import g
import os

db_abs_path = os.path.dirname(os.path.realpath(__file__))


# singleton design pattern
def get_db():
    db = getattr(g, '_database', None)

    if db is None:
        db = g.database = sqlite3.connect(os.path.join(db_abs_path, 'database', 'alegrosz.db'))
    return db
