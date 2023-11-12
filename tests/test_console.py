#!/usr/bin/python3
"""testing"""
import unittest
from unittest.mock import patch
import os
from io import StringIO
import sys
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

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
            "Usage : <class name>.update(<id>, <attribute name>,"
            " <attribute value>)\n"
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
        pat = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9 a-f]{12}"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_create_User(self):
        """Test creating a User instance"""
        pat = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_show_BaseModel(self):
        """ test_show_BaseModel """
        inst = BaseModel()
        pat = r"\[BaseModel\] \({id}\) {{'id': '{id}', 'created_at': '{created_at}', 'updated_at': '{updated_at}'}}"
        self.assertEqual(type(inst.id), str)
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(f"show BaseModel {inst.id}"))
            self.assertEqual(output.getvalue().strip(), "** no instance found **")

    def test_destroy_BaseModel(self):
        """testing the destroy command"""
        inst1 = BaseModel()
        command = f"destroy BaseModel {inst1.id}"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(output.getvalue().strip(), "** no instance found **")

    def test_all_BaseModel(self):
        """testing the all command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\[BaseModel\] \({id}\) {{'id': '{id}', 'created_at': '{created_at}', 'updated_at': '{updated_at}'}}"
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_BaseModel_all(self):
        """testing the BaseModel.all() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = "[BaseModel] ({id}\) {{'id': '{id}', 'created_at': '{created_at}', 'updated_at': '{updated_at}'}}"
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertRegex(output.getvalue().strip(), pat)
    
    def test_create_Review(self):
        """Test creating a Review instance"""
        pat = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_create_State(self):
        """Test creating a State instance"""
        pat = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_create_City(self):
        """Test creating a City instance"""
        pat = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_create_Amenity(self):
        """Test creating an Amenity instance"""
        pat = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_create_Place(self):
        """Test creating a Place instance"""
        pat = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_Review_all(self):
        """testing the Review.all() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\[Review\] \({id}\) {{'id': '{id}', 'created_at': '{created_at}', 'updated_at': '{updated_at}'}}"
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_User_all(self):
        """testing the User.all() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\[User\] \({id}\) {{'id': '{id}', 'created_at': '{created_at}', 'updated_at': '{updated_at}'}}"
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_State_all(self):
        """testing the State.all command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\[State\] \({id}\) {{'id': '{id}', 'created_at': '{created_at}', 'updated_at': '{updated_at}'}}"
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_City_all(self):
        """testing the City.all() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\[City\] \({id}\) {{'id': '{id}', 'created_at': '{created_at}', 'updated_at': '{updated_at}'}}"
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_Amenity_all(self):
        """testing the Amenity.all() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\[Amenity\] \({id}\) {{'id': '{id}', 'created_at': '{created_at}', 'updated_at': '{updated_at}'}}"
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_Place_all(self):
        """testing the Place.all() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\[Place\] \({id}\) {{'id': '{id}', 'created_at': '{created_at}', 'updated_at': '{updated_at}'}}"
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertRegex(output.getvalue().strip(), pat)
    
    def test_Review_show(self):
        """testing the Review.show() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\[Review\] \({id}\) {{'id': '{id}', 'created_at': '{created_at}', 'updated_at': '{updated_at}'}}"
            self.assertFalse(HBNBCommand().onecmd("Review.show()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_User_show(self):
        """testing the User.show() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\[User\] \({id}\) {{'id': '{id}', 'created_at': '{created_at}', 'updated_at': '{updated_at}'}}"
            self.assertFalse(HBNBCommand().onecmd("User.show()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_State_show(self):
        """testing the State.show command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\[State\] \({id}\) {{'id': '{id}', 'created_at': '{created_at}', 'updated_at': '{updated_at}'}}"
            self.assertFalse(HBNBCommand().onecmd("State.show()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_City_show(self):
        """testing the City.show() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\[City\] \({id}\) {{'id': '{id}', 'created_at': '{created_at}', 'updated_at': '{updated_at}'}}"
            self.assertFalse(HBNBCommand().onecmd("City.show()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_Amenity_show(self):
        """testing the Amenity.show() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\[Amenity\] \({id}\) {{'id': '{id}', 'created_at': '{created_at}', 'updated_at': '{updated_at}'}}"
            self.assertFalse(HBNBCommand().onecmd("Amenity.show()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_Place_show(self):
        """testing the Place.show() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\[Place\] \({id}\) {{'id': '{id}', 'created_at': '{created_at}', 'updated_at': '{updated_at}'}}"
            self.assertFalse(HBNBCommand().onecmd("Place.show()"))
            self.assertRegex(output.getvalue().strip(), pat)
    
    def test_Review_count(self):
        """testing the Review.count() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\d+"
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_User_count(self):
        """testing the User.count() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\d+"
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_State_count(self):
        """testing the State.count command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\d+"
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_City_count(self):
        """testing the City.count() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\d+"
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_Amenity_count(self):
        """testing the Amenity.count() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\d+"
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_Place_count(self):
        """testing the Place.count() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\d+"
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_update_BaseModel(self):
        """testing the Place.count() command """
        bm_obj = BaseModel()
        id = bm_obj.id
        command = f'BaseModel.update("{id}", "age", "20")'
        self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(bm_obj.age, "20")
        
    def test_update_User(self):
        """testing the Place.count() command """
        bm_obj = User()
        id = bm_obj.id
        command = f'User.update("{id}", "age", "20")'
        self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(bm_obj.age, "20")


if __name__ == "__main__":
    unittest.main()

