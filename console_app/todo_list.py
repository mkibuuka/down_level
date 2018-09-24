
from core.tasks import ToDo


class ToDoList(object):
    """
    A class that defines the attributes for a Todolist
    """

    # list_id = 0
    todo_lists = []

    def __init__(self, title):
        self.title = title
        self.todos = ToDo.todos

    def insert_todo_list(self, lst):
        """
        save/append a new todo object into the todos list

        Arguments:
            lst {[list]} -- todo-list object
        """
        self.todo_lists.append(lst)
        # print response to the console
        print(lst.title + ' successfully created')

    @classmethod
    def delete_todo_list(cls, title):
        if len(cls.todo_lists) == 0:
            print('no lists available')
            return 'no lists available'

        for l in cls.todo_lists:
            if l.title == title:
                print(l.title)
                cls.todo_lists.remove(l)
                print(cls.todo_lists)
            # print response to the console
            print('list named ' + title + ' doesnot exist')
            # return response after the method call
            return 'list named ' + title + ' doesnot exist'
