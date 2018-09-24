from core.accounts import User
from core.tasks import ToDo
from core.todo_list import ToDoList


# Helper functions
def user_signup_and_login():
    # get the username from the user
    username = input('Please provide a username: ')
    # check if the user has provided a name
    # if true then prompt the user for an email address
    if username:
        email = input('Please provide a email: ')
    else:
        print('You must provide a username')
        return
    # check if the user has provided an email address
    # if true then prompt the user for a password
    if email:
        password = input('Please provide a password: ')
    # else still prompt the user for an email address
    else:
        print('You must provide an email address')
        return
    # if password is provided, use the provided credentials
    # to login by calling the add_account method on the user class to
    # create a new user account
    if password:
        User.add_account(username=username, email=email, password=password)
        print(username + ' has successfully signed up')
    # else still prompt the user for a password
    else:
        print('You must provide a password')
        return

    # if the user has been successfully created, then ask the
    # user user if he would like to login into his new account
    print('Do you want to login into your new account?')
    login = input('Enter (y/n):')
    # if yes, then call the user_login helper method to login the user
    if login == 'y':
        user_login()
    # if not, thank the user for creating an account and return
    if login == 'n':
        print('Thank you for creating your first todo-list account')


def user_login():
    # get the username from the user
    username = input('Please provide a username: ')
    # check if the user has provided a name
    # if true then prompt the user for a password
    if username:
        password = input('Please provide a password: ')
    # else still prompt the user for the username
    else:
        print('You must provide a username!')
        return

    if password:
        # if password is provided, use the provided credentials
        # to login by calling the login method on the user class
        # to login the user
        response = User.login(username)
        if isinstance(response, bool):
            print(username + ' has successfully logged in')
        # then prompt the user to perform task functions
            todo_functions()
        # else if the we get a key error then use the provided
        # return a message to the user
        else:
            print('user ' + username + ' doesnot exist')
        # else if no password is provided then prompt the user for a password
    else:
        print('You must provide a password')
        return


def todo_functions():
    print('1.Create a todo_list')
    print('2.Delete list')
    print('3.Create a todo_item')
    print('4.Fetch a todo_item')
    print('5.Edit todo_item')
    print('6.Delete todo_item')
    print('7.Deate all todo_items')

    choice = int(input('select a choice from the above options:'))
    if choice == 1:
        new_todo_list()

    if choice == 2:
        delete_list()

    if choice == 3:
        new_todo_item()
        choice = input('would you like to add another todo item? (y/n):')
        while choice == 'y':
            new_todo_item()
            choice = input('would you like to add another todo item? (y/n):')
        choice = input('would you like to fetch your todo item? (y/n):')
        if choice == 'y':
            fetch_todo_item()
        choice = input('would you like to edit your todo item? (y/n):')
        if choice == 'y':
            edit_todo_item()
        choice = input('would you like to delete your todo item? (y/n):')
        if choice == 'y':
            delete_todo_item()

    if choice == 4:
        fetch_todo_item()

    if choice == 5:
        edit_todo_item()

    if choice == 6:
        delete_todo_item()

    if choice == 7:
        delete_all_items()


def new_todo_list():
    title = input('Enter a todo_list title:')
    if title:
        todo_list = ToDoList(title=title)
        todo_list.insert_todo_list(todo_list)


def delete_list():
    title = input('Enter a list title to delete:')
    ToDoList.delete_todo_list(title)


def new_todo_item():
    body = input('Enter a todo_item body:')
    if body:
        todo_item = ToDo(body=body)
        todo_item.insert_todo(todo_item)


def fetch_todo_item():
    body = input('Enter a todo_item body to search for:')
    if body:
        ToDo.get_todo_by_body(body)


def edit_todo_item():

    body = input('Enter a todo_item body to search for:')
    done = input('Enter true to mark the todo_item as done:')
    if body:
        ToDo.mark_todo_as_done(body, done)


def delete_todo_item():
    body = input('Enter a todo_item body:')
    if body:
        ToDo.delete_todo(body)


def delete_all_items():
    ToDo.delete_all_todos()


# Console implementation function
def user_input():

    print('Welcome to your todo-list app')
    print('1.sign up')
    print('2.login')

    choice = int(input('select a choice from the above options:'))
    if choice == 1:
        user_signup()

    if choice == 2:
        user_login()


if __name__ == '__main__':
    user_input()
