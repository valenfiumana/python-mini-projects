from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key) # now I use this as my key


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip() # strip \n
            user, psw = data.split("|") # user, psw = ["user", "psw"]
            print("User: ", user, " | Password: ",
                fer.decrypt(psw.encode()).decode())

def add():
    name = input('Account name: ')
    pwd = input("Password: ")

    with open('password.txt', 'a') as f: # a mode adds something to the end of the file if it exists or creates the file if it doesn't
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") # decode() makes it a string

while True:
    mode = input("Would you like to add a new password or view existing ones? (A, V). Press q to quit. ")
    if mode == "q":
        break
    if mode == "V":
        view()
    elif mode == "A":
        add()
    else:
        print("Invalid mode.")
        continue