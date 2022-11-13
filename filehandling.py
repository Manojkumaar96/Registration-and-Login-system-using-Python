import os.path
import re
import os

FILE_PATH = "C:\\Users\\manoj\\PycharmProjects\\GuviTasks\\database.txt"
#FILE_PATH = "c:\\database.txt"


def create_db():
    if not os.path.isfile(FILE_PATH):
        with open(FILE_PATH, "w"):
            pass


def get_db_to_dict():
    db_dict = {}
    with open(FILE_PATH, "r") as f:
        data = f.readlines()
    for line in data:
        email, password = line.split()
        db_dict[email] = password
    return db_dict


def update_db(email, password):
    with open(FILE_PATH, "r+") as f:
        db = f.read()
        replace = ' '.join([email, password])
        db_updated = re.sub("{}\s.+".format(email), replace, db)
        f.seek(0)
        f.truncate()
        f.write(db_updated)


def add_credential_to_db(email, password):
    with open(FILE_PATH, "a") as f:
        line = ' '.join([email, password])
        f.write(line)
        f.write("\n")


def check_email_present_in_db(email):
    db_dict = get_db_to_dict()
    res = email in db_dict
    return res


def check_password_for_email_id(email, password):
    db_dict = get_db_to_dict()
    res = db_dict[email] == password
    return res


def check_email_is_valid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    res = re.match(regex, email) is not None
    if not res:
        print("Invalid Email !")
    return res


def check_password_is_vaild(password):
    regex = re.compile(r"[A-Za-z0-9@#$%^&+=]{8,}")
    res = re.match(regex, password) is not None
    return res


def set_new_password(email):
    password = add_password()
    to_continue = True
    if password:
        update_db(email, password)
        print ("### Successfully updated new password ! ###")
        return not to_continue
    else:
        return to_continue


def handle_invalid_email_input_in_login():
    print ("Invalid Email ID, Please choose below option")
    to_continue = True
    while to_continue:
        print ("1. Login with correct Email \n"
               "2. Exit \n")
        user_input = input("Choose :")
        if user_input == "1":
            to_continue = login_fun()
        elif user_input == "2":
            print ("Thank you !!")
            to_continue = False


def handle_incorrect_password(email):
    print ("\n ### Incorrect Password ! ###")
    to_continue = True
    while to_continue:
        print ("please select any one option number\n"
               "1. Set New password \n"
               "2. Exit \n")
        user_input = input("Choose :")
        if user_input == "1":
            to_continue = set_new_password(email)
        elif user_input == "2":
            to_continue = False


def login_fun():
    print ("\n### Welcome to Login Page ! ###")
    email = input("Enter Email ID : ")
    if check_email_present_in_db(email):
        password = input("Enter Password : ")
        if check_password_for_email_id(email, password):
            print ("\nLogin Successful")
            print ("Exiting for your page !!\n")
            to_continue = False
            return to_continue
        else:
            handle_incorrect_password(email)
    else:
        handle_invalid_email_input_in_login()


def add_email():
    email = input("Enter Email ID :")
    is_email_valid = check_email_is_valid(email)
    db_dict = get_db_to_dict()
    if email in db_dict:
        print ("Email ID already exist")
        is_email_valid = False
    if not is_email_valid:
        print ("please select any one option number\n"
               "1. Enter EMail ID again \n"
               "2. exit \n")
        user_input = input("Choose Option : ")
        if user_input == "1":
            add_email()
        elif user_input == "2":
            email = None
    return email


def add_password():
    password = input("Enter password ID :")
    is_password_valid = check_password_is_vaild(password)
    if not is_password_valid:
        print("Invalid Password Format ! "
              "At least 1 Upper, lower, digit & special cases should be there"
              "Minimum 8 characters")
        print ("please select any one option number\n"
               "1. Enter Password again \n"
               "2. exit \n")
        user_input = input("Choose Option : ")
        if user_input == "1":
            add_password()
        elif user_input == "2":
            password = None
    return password


def register_fun():
    print ("\n### Welcome To Registration ! ###")
    email = add_email()
    if email:
        password = add_password()
        if password:
            add_credential_to_db(email, password)
            print ("### Successfully registered ! ###\n")
        else:
            print ("Registration failed")
    else:
        print ("Registration failed")


def user_opt():
    to_continue = True
    while to_continue:
        print ("\n### please select any one option number ###\n"
               "1. Login to site\n"
               "2. New Register \n"
               "3. Exit from Site")
        user_input = input("Choose :")
        if user_input == "1":
            login_fun()
        elif user_input == "2":
            register_fun()
        elif user_input == "3":
            print ("Thank you !!")
            to_continue = False
        else:
            print ("Invalid input Option ! \n")
            continue


def main():
    create_db()
    print ("######################### Welcome to Web Site ###########################\n")
    user_opt()


if __name__ == "__main__":
    main()
