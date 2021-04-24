import random
database = {}

def init():
    print('***************** Welcome to Our Bank ******************')
    haveAcct()
def genAcct():
    return random.randrange(1111111111,9999999999)

def option():
    action = int(input('Please choose a transaction:''\n' '1 - Withdrawl ''\n' '2 - Deposit ''\n' '3 - Complaint ''\n' '4 - Exit ' '\n'))
    if(action == 1):
        print(input('Enter Withdrawl amount:' '\n'))
        print('Please take your Cash from the slot' '\n')
        option()  
    elif(action == 2):
        print(input('Enter Deposit amount:' '\n'))
        print('Please insert your Deposit in the slot' '\n')
        option()
    elif(action == 3): 
        print(input('Please detail your Complaint:' '\n'))
        print('\n''Thank you; your Complaint has been submitted' '\n')
        option()
    elif(action == 4): 
        print('Thank you for Banking with us.')
        haveAcct()
def login():
    authUsers = ['Fernando','Seyi','fapra']
    authPassword = ['passFern','passSeyi','passfapra']
    name = input('To perform a transaction please enter userId:''\n')
    userId = authUsers.index(name) 
    if(name in authUsers): 
        print('Please enter password: ')
    password = input()
    if(password == authPassword[userId]):
        import datetime 
        datetime_object = datetime.datetime.now()
        print(datetime_object.strftime('\n''%x''\n''%I:%M ''%p''\n'))
        print('Welcome %s' % name) 
        option()
acctNum = genAcct()
#fname = input()
#lname = input()
#email = input()
#userId = input()
#password = input()
def signUp():
    fname = input('To Open an account Please Enter First name: ' '\n')
    lname = input('Please Enter Last name: ' '\n')
    email = input('Please Enter Email:' '\n')
    userId = input('Please choose a UserId: ' '\n')
    password = input('Please create a Password: ' '\n')
    genAcct()
    print('Your new Accout Number is: ')
    print(acctNum)
    option()
def haveAcct():
    print('\n')
    haveAcct = int(input('Are you an existing Account owner? ''\n''\n''Enter: 1 - Yes or 2 - No' '\n''\n'))
    if(haveAcct == 1):
        print('\n')
        login()
    elif(haveAcct == 2):
        print('\n')
        signUp()

init()