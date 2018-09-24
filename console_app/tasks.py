class ToDo(object):
    """
    Class that defines attributes for a ToDo object.
    """
    # list object to store todo items
    todos = []

    def __init__(self, body):
        self.body = body
        self.done = False

    def insert_todo(self, todo):

        """
        save/append a new todo object into the todos list

        Arguments:
           todo {[ToDo]} -- A todo object
        """

        self.todos.append(todo)
        # print response to the console
        print('Todo_item ' + (self.todos[0].body) + ' created successfully')
        # return response after the method call
        return 'Todo_item ' + (self.todos[0].body) + ' created successfully'

    @classmethod
    def get_todo_by_body(cls, body):
        # check if todos list is empty
        if len(cls.todos) == 0:
            # print response to the console
            print('no items available')
            # return response after the method call
            return 'no items available'
        # iterate through the todos list to find the matching item
        for tdo in cls.todos:
            if tdo.body == body:
                return tdo
            # print response to the console
            print('todo_item does not exist')
            # return response after the method call
            return 'todo_item does not exist'

    @classmethod
    def delete_todo(cls, body):
        """
        Delete a todo item from the list

        Arguments:
            todo {[ToDo]} -- A todo object
        """
        # check if todos list is empty
        if len(cls.todos) == 0:
            # print response to the console
            print('no items available')
            # return response after the method call
            return 'no items available'
        # iterate through the todos list to find the matching item
        for t in cls.todos:
            if t.body == body:
                cls.todos.remove(t)
                # print response to the console
                print('Todo_item ' + body + ' deleted successfully')
                # return response after the method call
                return 'Todo_item ' + body + ' deleted successfully'

    @classmethod
    def mark_todo_as_done(cls, body, done):
        """
        Mark  a todo item as done

        Arguments:
            todo {[ToDo]} -- A todo object
        """
        # iterate through the todos list to find the matching item
        for tdo in cls.todos:
            if tdo.body == body:
                if done is not None and tdo.done is False:
                    tdo.done = done
                    # print response to the console
                    print('done:', tdo.done)
                    # return response after the method call
                    return tdo

    @classmethod
    def delete_all_todos(cls):
        """
        Delete all todos

        """
        # check if todos list is empty
        if len(cls.todos) == 0:
            # print response to the console
            print('no items available')
            # return response after the method call
            return 'no items available'
        # delete all todo-items in the todos list
        cls.todos.clear()
        # print response to the console
        print('All items cleared')
        # return response after the method call
        return cls.todos
