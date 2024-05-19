#!/usr/bin/python3
"""Test cases for user"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User"""

    def test_User_instance(self):
        """Test if User is an instance of BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
    
    def test_user_attributes(self):
        """Test the attributes of User"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))
        
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_user_attribute_values(self):
        """Test setting and getting values of User attributes"""
        user = User()
        user.email = "user@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "user@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

if __name__ == '__main__':
    unittest.main()
