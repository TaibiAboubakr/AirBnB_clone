#!/usr/bin/python3
"""testing"""
import unittest
from unittest.mock import patch
import os
from io import StringIO
import sys
from console import HBNBCommand


class TesttheHBNBPrompt(unittest.TestCase):
    """testing the hbnb prompt and the emptyline"""
    def test_prompt_string(self):
        self.assertEqual("(hbnb)", HBNBCommand.prompt)

    def test_prompt_empty_line(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommandEntryPoint(unittest.TestCase):
    """testing the entry point of the command interpreter containing
        EOF, quit, create, show, all, destroy, and update commands"""
    def test_EOF(self):
        use = "signal to exit the program using CTRL+D"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(use, output.getvalue().strip())

    def test_quit(self):
        use = "Quit command to quit the program"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(use, output.getvalue().strip())

    def test_create(self):
        use = (
                "create <class>\n"
                "creates a new instance id")
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(" help create"))
            self.assertEqual(use, output.getvalue().strip())

    def test_show(self):
        use = (
                "show <class> <instance id>\n"
                "shows the class created")
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(" help show"))
            self.assertEqual(use, output.getvalue().strip())

    def test_destroy(self):
        use = (
                "destroy <class> <isntance id>\n"
                "deletes the class and its instance id")
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(" help destroy"))
            self.assertEqual(use, output.getvalue().strip())

    def test_all(self):
        use = (
                "all or  all <class>\n"
                "shows all classes and instances created")
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(use, output.getvalue().strip())

    def test_update(self):
        use = (
                "update <class> <id> <attribute name> \"<attribute value>\"\n"
                "updates an instance by adding new\n"
                "attributes or updating existing ones")
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(use, output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
