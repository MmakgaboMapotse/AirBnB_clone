#!/usr/bin/python3
"""Initializes the FileStorage instance for the models directory."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
