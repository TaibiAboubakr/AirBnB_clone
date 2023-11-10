#!/usr/bin/python3
"""testing"""
import unittest
from unittest.mock import patch
import os
from io import StringIO
import sys
from console import HBNBCommand

""" TesttheHBNBPrompt class """


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
        use = "Quit command to exit the program"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(use, output.getvalue().strip())

    def test_create(self):
        use = (
                "create <class>\n"
                "create a new instance")
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
                "deletes an instance based on the class name and id\n"
                "(save the change into the JSON file)")
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(" help destroy"))
            self.assertEqual(use, output.getvalue().strip())

    def test_all(self):
        use = (
                "all or all <class>\n"
                "all : show all instances created for all classes\n"
                "all <class> : show all instances for specific class")
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(use, output.getvalue().strip())
    
    def test_count(self):
        use = (
                "Usage : <class name>.count().\n"
                "command to retrieve the number of instances of a class")
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(use, output.getvalue().strip())

    def test_update(self):
        use = (
                "Usage : update <class> <id> <attribute name> <attribute value>\n"
                "Usage : <class name>.update(<id>, <attribute name>, <attribute value>)\n"
                "Usage : <class name>.update(<id>, <dictionary representation>)\n"
                "Updates an instance based on the class name\n"
                "and id by adding or updating attribute")
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(use, output.getvalue().strip())

    def test_quit_1(self):
        """ test_quit_1 """
        with patch('sys.stdout', new=StringIO()) as output:
            try:
                HBNBCommand().onecmd("quit")
            except SystemExit:
                pass
            self.assertEqual("", output.getvalue().strip())

    def test_emptyline(self):
        """ test_emptyline"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_create_BaseModel(self):
        """ test_create_BaseModel """
        pat = r"[0-9 a-f]{8}-[0-9 a-f]{4}-[0-9 a-f]{4}-[0-9 a-f]{4}-[0-9 a-f]{12}"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertRegex(output.getvalue().strip(), pat)
if __name__ == "__main__":
    unittest.main()
