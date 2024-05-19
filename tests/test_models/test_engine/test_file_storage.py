#!/usr/bin/python3
"""
Test suite for file_storage engine
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage
import os


class TestFileStorage(unittest.TestCase):
    def test_attrs(self):
        base = BaseModel()
        storage = FileStorage()
        with self.assertRaises(AttributeError):
            file_path = storage.file_path
        with self.assertRaises(AttributeError):
            file_path = storage.__file_path
        with self.assertRaises(AttributeError):
            file_path = storage.objects
        with self.assertRaises(AttributeError):
            file_path = storage.__objects

        with self.assertRaises(AttributeError):
            FileStorage.file_path
        with self.assertRaises(AttributeError):
            FileStorage.__file_path
        with self.assertRaises(AttributeError):
            FileStorage.objects
        with self.assertRaises(AttributeError):
            FileStorage.__objects

    def test_reload(self):
        storage1 = FileStorage()
        base1 = BaseModel({id: 8})
        base1.save()
        storage.save()
        self.assertEqual(storage.reload(), None)

    def test_all(self):
        storage1 = FileStorage()
        self.assertIsInstance(storage1.all(), dict)
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        storage1 = FileStorage()
        base = BaseModel()
        storage1.new(base)
        key = type(base).__name__ + '.' + base.id
        self.assertEqual(storage1.all()[key], base)

    def test_save(self):
        storage1 = FileStorage()
        base = BaseModel()
        storage1.new(base)
        storage1.save()
        self.assertTrue(os.path.isfile('file.json'))
