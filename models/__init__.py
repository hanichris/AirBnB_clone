#!/usr/bin/env python3
""" Module to enable access to file storage """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
