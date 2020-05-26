import os
from datetime import datetime
from secrets import token_hex
from werkzeug.utils import secure_filename

basedir = os.path.dirname(os.path.abspath(__file__))
uploads_path = os.path.join(basedir, "..", "..", "uploads")


def save_image_upload(image):
    format = "%Y%m%dT%H%M%S"
    now = datetime.utcnow().strftime(format)
    random_string = token_hex(2)
    filename = f"{random_string}_{now}_{image.filename}"
    filename = secure_filename(filename)
    image.save(os.path.join(uploads_path, filename))
    return filename
