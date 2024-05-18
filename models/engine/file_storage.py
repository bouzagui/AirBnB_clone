#!/usr/bin/python3
""" recreate a BaseModel """
import cmd

class FileStorage:
    def __init__(self, *args, **kwargs):
        __file_path = kwargs.('file_path')
