#!/usr/bin/python3
"""Test cases for user"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City"""

    def test_City_instance(self):
        """Test if City is an instance of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_City_attributes(self):
        """Test the attributes of City"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))

    def test_City_attribute_values(self):
        """Test setting and getting values of City attributes"""
        city = City()
        city.state_id = "CA"
        city.name = "San Francisco"
        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")
