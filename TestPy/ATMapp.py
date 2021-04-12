name = input("Please enter name: \n")
authUsers = ['Fernando','Seyi','fapra']
authPassword = ['passFern','passSeyi','passfapra']
if(name in authUsers):
    userId = authUsers.index(name)
    password = input('Please enter password' '\n')
    if(password == authPassword[userId]):
        import datetime
        datetime_object = datetime.datetime.now()
        print(datetime_object.strftime('\n''%x''\n''%I:%M ''%p''\n'))
        print('Welcome %s' % name)
        print('Please choose an option: \n')
        print('1 - Withdrawl \n''2 - Deposit \n''3 - Complaint' '\n' '4 - Exit' '\n')
        Option = int(input('Option:'))
        if(Option == 1 or OptionRecall == 1):
            Withdrawl = int(input('Enter Withdrawl amount:' '\n'))
            print('Please take your Cash from the slot' '\n')
            print('\n''Please choose an option: \n')
            print('1 - Withdrawl \n''2 - Deposit \n''3 - Complaint' '\n' '4 - Exit' '\n')      
            OptionRecall = int(input('Option:'))
        if(Option == 2 or OptionRecall == 2):
            Deposit = int(input('Enter Deposit amount:' '\n'))
            print('Please insert your Deposit in the slot' '\n')
            print('\n''Please choose an option: \n')
            print('1 - Withdrawl \n''2 - Deposit \n''3 - Complaint' '\n' '4 - Exit' '\n')
            OptionRecall = int(input('Option:'))
        if(Option == 3 or OptionRecall == 3):
            Complaint = str(input('Please detail your Complaint:' '\n'))
            print('\n''Thank you; your Complaint has been submitted' '\n')
            print('\n''Please choose an option: \n')
            print('1 - Withdrawl \n''2 - Deposit \n''3 - Complaint' '\n' '4 - Exit' '\n')
            OptionRecall = int(input('Option:'))
        if(Option == 4 or OptionRecall == 4):
            Exit = (print('Thank you for Banking with us.'))
    else:
        print('Incorrect Password \n''Please try again' '\n')
else:
    print('Name not Authorized' '\n''Please Try Again' '\n') 
     
