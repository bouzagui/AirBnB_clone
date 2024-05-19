#!/usr/bin/python3
"""Test suite for base_model"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from unittest.mock import patch


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel"""

    def setUp(self):
        """Set up test methods"""
        self.base = BaseModel()

    def test_str(self):
        """Checks the string representation of an instance"""
        expected_str = f"[{type(self.base).__name__}] ({self.base.id}) {self.base.__dict__}"
        self.assertEqual(str(self.base), expected_str)

    def test_to_dict(self):
        """Checks the to_dict() method"""
        base_dict = self.base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict['__class__'], 'BaseModel')
        self.assertEqual(base_dict['id'], self.base.id)
        self.assertEqual(base_dict['created_at'], self.base.created_at.isoformat())
        self.assertEqual(base_dict['updated_at'], self.base.updated_at.isoformat())

        prev_time = self.base.updated_at
        self.base.save()
        self.assertNotEqual(prev_time, self.base.updated_at)

    def test_attr_classes(self):
        """Checks if attributes are of the correct type"""
        self.assertIsInstance(self.base.id, str)
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)

        base2 = BaseModel()
        self.assertNotEqual(self.base.id, base2.id)

    def test_save(self):
        """Tests the save method"""
        prev_time = self.base.updated_at
        self.base.save()
        new_time = self.base.updated_at
        self.assertNotEqual(prev_time, new_time)

if __name__ == '__main__':
    unittest.main()
