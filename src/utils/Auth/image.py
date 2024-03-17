import os
import shutil
from uuid import uuid4

from core.config import config


def save_image(file):
    file_name = uuid4().hex + "." + file.filename.split(".")[-1]
    file_path = config.PROJECT_ROOT_DIR + "/media/" + file_name
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return file_name


def delete_image(file_name):
    file_path = config.PROJECT_ROOT_DIR + "/media/" + file_name
    if os.path.exists(file_path):
        os.remove(file_path)
