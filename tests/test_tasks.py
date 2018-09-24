from unittest import TestCase
from core.tasks import ToDo


class TestToDo_1(TestCase):
    """
    Test class for testing todo_items create,
    insert/save and fetch methods

    """
    def setUp(self):
        self.todo_1 = ToDo('test commandline application')

    def test_create_todo_item(self):
        self.assertIsInstance(self.todo_1, ToDo)
        self.assertEqual(self.todo_1.body, 'test commandline application')

    def test_get_todo_item_before_insertion(self):
        todo = ToDo.get_todo_by_body(self.todo_1.body)
        self.assertEqual(todo, 'no items available')

    def test_insert_todo_item(self):
        message = self.todo_1.insert_todo(self.todo_1)
        self.assertEqual(message, 'Todo_item test commandline application created successfully')

    def test_to_fetch_todo_item(self):
        self.todo_1.insert_todo(self.todo_1)
        todo = ToDo.get_todo_by_body(self.todo_1.body)

        self.assertIsInstance(todo, ToDo)
        self.assertEqual(todo.body, 'test commandline application')

    def test_to_fetch_todo_item_with_unknown_body(self):
        todo = ToDo.get_todo_by_body('perfect writting unittests in python')
        self.assertEqual(todo, 'todo_item does not exist')


class TestToDo_2(TestCase):
    """
    Test class for testing todo_items edit,
    delete single todo_item and delete all todo_items

    """
    def setUp(self):
        self.todo_2 = ToDo('separating test cases')

    def test_edit_todo_item(self):
        self.todo_2.insert_todo(self.todo_2)
        todo = ToDo.mark_todo_as_done(self.todo_2.body, done=True)
        self.assertIsInstance(todo, ToDo)
        self.assertEqual(todo.done, True)

    def test_successful_delete_todo_item(self):
        message = ToDo.delete_todo(self.todo_2.body)
        self.assertEqual(message, 'Todo_item separating test cases deleted successfully')

    def test_to_delete_all_todo_items(self):
        response = ToDo.delete_all_todos()

        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 0)
