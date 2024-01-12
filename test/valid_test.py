
def email_validator():
    from schema.user_schema import UserRegister
    email = 'apple@apple.com'
    username = 'panda'
    password = '123456'
    test = UserRegister(email=email, username=username, password=password)


if __name__ == '__main__':
    email_validator()

