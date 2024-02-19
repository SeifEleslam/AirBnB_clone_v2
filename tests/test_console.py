#!/usr/bin/python3
"""Console Test"""

from io import StringIO
import unittest

from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestConsole(unittest.TestCase):
    """TestConsole"""

    def test_create_cmd(self):
        """test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            model = storage.all()["BaseModel."+f.getvalue().strip()]
            self.assertIsNotNone(model)
            self.assertIsInstance(model, BaseModel)
        arg_name = 'first_name'
        arg_val = 'bad'
        with patch('sys.stdout', new=StringIO()) as f:
            curr = len(storage.all())
            self.assertFalse(HBNBCommand().onecmd(
                "create User {}=\"{}\"".format(arg_name, arg_val)))
            new = len(storage.all())
            model = storage.all()["User."+f.getvalue().strip()]
            self.assertIsNotNone(model)
            self.assertIsInstance(model, User)
            self.assertEqual(getattr(model, arg_name), arg_val)
            self.assertEqual(new - curr, 1)

        output = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseMode"))
            self.assertEqual(f.getvalue().strip(), output)
        output = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(f.getvalue().strip(), output)
