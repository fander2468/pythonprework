def hello_name (username):
    return 'Hello ' + username.title()


while True:
    print('Please enter your username: ')
    name = input('Username:')
    user_input = hello_name(name)
    print(user_input)