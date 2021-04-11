name = input("Please enter name: \n")
authUsers = ['Fernando','Seyi','fapra']
authPassword = ['passFern','passSeyi','passfapra']
if(name in authUsers):
    userId = authUsers.index(name)
    password = input('Please enter password' '\n')
    if(password == authPassword[userId]):
        print('\n' 'Welcome %s' % name)
        print('Please choose an option: \n')
        print('1 - Withdrawl \n''2 - Deposit \n''3 - Complaint' '\n')
        Option = int(input('Option:'))
        if(Option == 1):
            Withdrawl = int(input('Enter Withdrawl amount:' '\n'))
            print('Please take your Cash from the slot' '\n')
        if(Option == 2):
            Deposit = int(input('Enter Deposit amount:' '\n'))
            print('Please insert your Deposit in the slot' '\n')
        if(Option == 3):
            Complaint = (input('Please detail your Complaint:' '\n'))
            print('\n''Thank you; your Complaint has been submitted' '\n')
    else:
        print('Incorrect Password \n''Please try again' '\n')
else:
    print('Name not Authorized' '\n''Please Try Again' '\n') 
     