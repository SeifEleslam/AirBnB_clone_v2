#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

if 'HBNB_TYPE_STORAGE' in os.environ and\
        os.environ['HBNB_TYPE_STORAGE'] == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
