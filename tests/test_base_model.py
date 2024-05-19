#!/usr/bin/python3
import unittest
from datetime import datetime, timedelta
from uuid import UUID
from models.base_model import BaseModel
"""unit testing for base model"""



class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up test methods."""
        self.model = BaseModel()

    def test_id_is_uuid(self):
        """Test if id is a valid UUID."""
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(UUID(self.model.id), UUID)

    def test_created_at_is_datetime(self):
        """Test if created_at is a datetime object."""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test if updated_at is a datetime object."""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_method(self):
        """Test the __str__ method."""
        string_rep = str(self.model)
        expected_str = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(string_rep, expected_str)

    def test_save_method(self):
        """Test the save method updates `updated_at`."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)
        self.assertTrue(self.model.updated_at > old_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method returns a correct dictionary representation."""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

    def test_kwargs_initialization(self):
        """Test initializing with kwargs."""
        dt_str = datetime.now().isoformat()
        kwargs = {
            'id': '1234',
            'created_at': dt_str,
            'updated_at': dt_str
        }
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, '1234')
        self.assertEqual(model.created_at, datetime.fromisoformat(dt_str))
        self.assertEqual(model.updated_at, datetime.fromisoformat(dt_str))

    def test_storage_new_called(self):
        """Test if storage.new() is called during initialization."""
        with unittest.mock.patch('basemodel.storage.new') as mock_storage_new:
            model = BaseModel()
            mock_storage_new.assert_called_with(model)

    def test_storage_save_called(self):
        """Test if storage.save() is called during save()."""
        with unittest.mock.patch('basemodel.storage.save') as mock_storage_save:
            self.model.save()
            mock_storage_save.assert_called()


if __name__ == '__main__':
    unittest.main()
