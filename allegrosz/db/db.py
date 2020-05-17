import sqlite3
import os

from flask import g


def get_db():
    """singleton (wzorzec projektowy)

    :return:
    """
    db = getattr(g, '__database__', None)


    if db is None:
        base_dir = os.path.abspath(os.path.dirname(__file__))
        db = g.__database = sqlite3.connect(os.path.join(base_dir, "allegrosz.db"))

    return db