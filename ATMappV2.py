import random
database = {}
def init():
    print('\n' 'Welcome to Our Bank ''\n')
init()
def login():
    name = input("Please enter userId:\\n")
authUsers = ['Fernando','Seyi','fapra'] 
authPassword = ['passFern','passSeyi','passfapra'] 
if(name in authUsers): 
    userId = authUsers.index(name)\ 
    print('Please enter password:')\ 
    password = (input())\ 
    if(password == authPassword[userId]):\ 
        import datetime\ 
        datetime_object = datetime.datetime.now()\ 
        print(datetime_object.strftime('\\n''%x''\\n''%I:%M ''%p''\\n'))\ 
        print('Welcome %s' % name)\ 
        print('Please choose a transaction: \\n')\ 
        print('1 - Withdrawl \\n''2 - Deposit \\n''3 - Complaint' '\\n' '4 - Exit' '\\n')\ 
        Option = int(input('Option: '));\ 
        if(Option == 1):\ 
            Withdrawl = (input('Enter Withdrawl amount:' '\\n'))\ 
            print('Please take your Cash from the slot' '\\n')\ 
            print('\\n''Please choose your next transaction: \\n')\ 
            print('1 - Withdrawl \\n''2 - Deposit \\n''3 - Complaint' '\\n' '4 - Exit' '\\n')\ 
            Option('\\n')\ 
            if(Option == 1):\ 
                Withdrawl = (input('Enter Withdrawl amount:' '\\n'))\ 
                print('Please take your Cash from the slot' '\\n')\ 
                print('\\n''Please choose your next transaction: \\n')\ 
                print('1 - Withdrawl \\n''2 - Deposit \\n''3 - Complaint' '\\n' '4 - Exit' '\\n')\ 
                Option('\\n')\ 
            elif(Option == 2):\ 
                Deposit = (input('Enter Deposit amount:' '\\n'))\ 
                print('Please insert your Deposit in the slot' '\\n')\ 
                print('Please choose your next transaction:' '\\n')\ 
                print('1 - Withdrawl \\n''2 - Deposit \\n''3 - Complaint' '\\n' '4 - Exit' '\\n')\ 
                Option('\\n')\ 
            elif(Option == 3):\ 
                Complaint = str(input('Please detail your Complaint:' '\\n'))\ 
                print('\\n''Thank you; your Complaint has been submitted' '\\n')\ 
                print('\\n''Please choose your next transaction: \\n')\ 
                print('1 - Withdrawl \\n''2 - Deposit \\n''3 - Complaint' '\\n' '4 - Exit' '\\n')\ 
                Option('\\n')\ 
            elif(Option == 4):\ 
                print('Thank you for Banking with us.')\ 
    print('To Login please enter your Username: ' )
    if(input == userId):
        print('Enter Password: ')
        if(input == password):
            print('Please choose an Option: 1 - Withdrawl, ')
def signUp():
    fname = input('To Open an account Please Enter First name: ' '\n')
    lname = input('Please Enter Last name: ' '\n')
    email = input('Please Enter Email:' '\n')
    userId = input('Please choose a Username: ' '\n')
    password = input('Please create a Password: ' '\n')
    database[acctNum] = [fname, lname, email, userId, password]
    genAcct()
def genAcct():
    random
    return random.randrange(1111111111,9999999999)
acctNum = genAcct()
haveAcct = int(input('Do you have an account? : 1 - Yes or 2 - No' '\n'))
if(haveAcct == 1):
    login()
elif(haveAcct == 2):
    signUp()
    genAcct()
    print('Your new Account Number is: ')
    print(acctNum)
else:
    print('Invalid option')
