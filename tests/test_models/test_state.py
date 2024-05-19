#!/usr/bin/python3
"""Test cases for user"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State"""

    def test_State_instance(self):
        """Test if State is an instance of BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_State_attributes(self):
        """Test the attributes of State"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertIsInstance(state.name, str)

    def test_State_attribute_values(self):
        """Test setting and getting values of State attributes"""
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")
