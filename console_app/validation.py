import re


def validate_user_signup(username, email, password):
    """This function should be called to validate
    provided sign-up form arguments

    Arguments:
        username {[str]} -- user's name
        email {[str]} -- user's email address
        password {[str]} -- user's password
    Returns:
        [bool] -- returns True if all values are valid
    """

    if not username or username == "" or username.isspace():
        return "Please provide a username"

    if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "invalid email or missing email address"

    if not password or not len(password) >= 8:
        return "missing password/password should be atleast 8 characters"
    return True


def validate_user_login(username, password):
    """
    This function should be called to validate
    user login form arguments

    Arguments:
        username {[str]} -- user's name
        password {[str]} -- user's password
    Returns:
        [bool] -- returns True if all values are valid
    """

    if not username or username == "" or username.isspace():
        return "Please provide a username"

    if not password or not len(password) >= 8:
        return "missing password/password should be atleast 8 characters"
    return True
