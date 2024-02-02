file_name = './secret_password.txt'
try:
    with open(file_name) as file_password:
        contents = file_password.read()
except FileNotFoundError:
    print(f"Sorry, the file {file_name} does not exist.")
else:
    # print(contents.strip())
    password_input = input('Enter your password:')
    if password_input == contents.strip():
        print('Access Granted')
    else:
        print('Access Denied')
