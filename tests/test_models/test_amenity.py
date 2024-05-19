#!/usr/bin/python3
"""Test cases for user"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity"""

    def test_amenity_instance(self):
        """Test if Amenity is an instance of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
    
    def test_amenity_attributes(self):
        """Test the attributes of Amenity"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertIsInstance(amenity.name, str)
    
    def test_amenity_attribute_values(self):
        """Test setting and getting values of Amenity attributes"""
        amenity = Amenity()
        amenity.name = "Wifi"
        self.assertEqual(amenity.name, "Wifi")
