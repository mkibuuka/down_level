from unittest import TestCase
from core.todo_list import ToDoList


class TestToDoList(TestCase):
    """
    Test class for testing todo_lists

    """
    def setUp(self):
        self.list_1 = ToDoList('Testing')

    def test_create_a_new_todo_list(self):

        self.assertIsInstance(self.list_1, ToDoList)
        self.assertIsInstance(self.list_1.todos, list)
        self.assertEqual(self.list_1.title, 'Testing')

    def test_non_successful_delete_empty_list(self):
        self.assertEqual(ToDoList.delete_todo_list('delete'), 'no lists available')

    def test_to_insert_new_todo_list(self):
        self.list_1.insert_todo_list(self.list_1)

        self.assertEqual(len(ToDoList.todo_lists), 1)
        self.assertEqual(ToDoList.todo_lists[0].title, 'Testing')
        self.assertEqual(len(ToDoList.todo_lists[0].todos), 0)

    def test_to_non_successful_delete_todo_list(self):
        self.assertEqual(ToDoList.delete_todo_list('delete'), 'list named delete doesnot exist')

    def test_to_to_successful_delete_todo_list(self):
        self.assertEqual(len(ToDoList.todo_lists), 1)
        ToDoList.delete_todo_list(self.list_1.title)
        self.assertEqual(len(ToDoList.todo_lists), 0)
