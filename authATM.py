# register
# - first name, last name, password, email
# - generate user account number


# login
# - account number & password


# bank operations

# Initializing the system
import random
import validation
import database
from getpass import getpass


def init():
    print("Welcome to bankPHP")

    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    else:
        print("You have selected invalid option")
        init()


def login():
    print("********* Login ***********")

    account_number_from_user = input("To Login, please enter your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("Please enter your password \n")

        user = database.authenticated_user(account_number_from_user, password)

        if user:
            bank_operation(user)

        else:
            print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


def register():
    print("****** Register *******")

    email = input("Please enter a valid email address \n")
    first_name = input("Enter your first name? \n")
    last_name = input("Enter your last name? \n")
    password = getpass("Create a password for yourself \n")

    account_number = generation_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        selected_option()

    else:
        print("Something went wrong, please try again")
        init()


def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))
    selected_option()

def selected_option():
    selected_option = input('Please choose a transaction:''\n' '1 - Withdrawal ''\n' '2 - Deposit ''\n' '3 - Comment ''\n' '4 - Logout ' '\n')

    if selected_option == 1:

        withdrawal_operation()
    elif selected_option == 2:

        deposit_operation()
    elif selected_option == 3:

        comment_operation()
    elif selected_option == 4:

        logout()
    else:

        print("Invalid option selected")
        selected_option()


def withdrawal_operation():
    print(input('Enter Withdrawal amount:' '\n'))
    print('Please take your Cash from the slot' '\n')
    selected_option()

    # get current balance
    # get amount to withdrawal
    # check if current balance > withdraw balance
    # deduct withdrawn amount form current balance
    # display current balance


def deposit_operation():
    print(input('Enter Deposit amount:' '\n'))
    print('Please insert your Deposit in the slot' '\n')
    selected_option()

    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance


def comment_operation():
    print(input('Please detail your comments:' '\n'))
    print('***** Thank you; your comments have been submitted *****' '\n')
    selected_option()


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]


def logout():
    print('Thank you for Banking with us.')
    login()


init()
