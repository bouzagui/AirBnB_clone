#!/usr/bin/python3
"""Test cases for user"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for user"""

    def test_User_instance(self):
        """Test if User is an instance of BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_review_attributes(self):
        """Test the attributes of Review"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

    def test_review_attribute_values(self):
        """Test setting and getting values of Review attributes"""
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "Example"
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Example")
