#!/usr/bin/python3
"""test module for console"""

import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage



class TestConsole(unittest.TestCase):
    """test class for console"""

    def test_console(self):
        """test console"""
        self.assertTrue(HBNBCommand())

    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up after test"""
        storage.all().clear()
        storage.save()



    def test_create_missing_class(self):
        """Test create command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd('create')
            self.assertEqual(output.getvalue().strip(), '** class name missing **')

    def test_create_invalid_class(self):
        """Test create command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd('create NonExistentClass')
            self.assertEqual(output.getvalue().strip(), '** class doesn\'t exist **')


    def test_show_missing_class(self):
        """Test show command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd('show')
            self.assertEqual(output.getvalue().strip(), '** class name missing **')

    def test_show_invalid_class(self):
        """Test show command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd('show NonExistentClass 1234')
            self.assertEqual(output.getvalue().strip(), '** class doesn\'t exist **')

    def test_show_missing_id(self):
        """Test show command with missing ID"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd('show BaseModel')
            self.assertEqual(output.getvalue().strip(), '** instance id missing **')

    def test_show_no_instance_found(self):
        """Test show command with non-existent instance ID"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd('show BaseModel 1234')
            self.assertEqual(output.getvalue().strip(), '** no instance found **')

if __name__ == '__main__':
    unittest.main()