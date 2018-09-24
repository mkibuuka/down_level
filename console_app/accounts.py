class User(object):
    """Class that defines attributes for a User object."""

    accounts = {}

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @classmethod
    def add_account(cls, username, email, password):
        user = User(username=username, email=email, password=password)
        cls.accounts[username] = user
        print(str(cls.accounts[username].email))

    @classmethod
    def login(cls, username):
        try:
            cls.accounts[username]
            return True
        except KeyError as e:
            return e
