import os
import subprocess

def execute_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout

def get_user_data(username):
    with open(f'/home/{username}/data.txt', 'r') as file:
        data = file.read()
    return data

def connect_to_db():
    db_password = 'password123'
    connection_string = f'mysql://root:{db_password}@localhost/dbname'
    os.system(f'mysql -e "USE dbname;"')

if __name__ == "__main__":
    print(execute_command('ls -l'))
    print(get_user_data('john'))
    connect_to_db()
