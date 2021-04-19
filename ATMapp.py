{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang1033{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 10.0.10586}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang9 name = input("Please enter userId:\\n")\par
authUsers = ['Fernando','Seyi','fapra']\par
authPassword = ['passFern','passSeyi','passfapra']\par
if(name in authUsers):\par
    userId = authUsers.index(name)\par
    print('Please enter password:')\par
    password = (input())\par
    if(password == authPassword[userId]):\par
        import datetime\par
        datetime_object = datetime.datetime.now()\par
        print(datetime_object.strftime('\\n''%x''\\n''%I:%M ''%p''\\n'))\par
        print('Welcome %s' % name)\par
        print('Please choose a transaction: \\n')\par
        print('1 - Withdrawl \\n''2 - Deposit \\n''3 - Complaint' '\\n' '4 - Exit' '\\n')\par
        Option = int(input('Option: '));\par
        if(Option == 1):\par
            Withdrawl = (input('Enter Withdrawl amount:' '\\n'))\par
            print('Please take your Cash from the slot' '\\n')\par
            print('\\n''Please choose your next transaction: \\n')\par
            print('1 - Withdrawl \\n''2 - Deposit \\n''3 - Complaint' '\\n' '4 - Exit' '\\n')\par
            Option('\\n')\par
            if(Option == 1):\par
                Withdrawl = (input('Enter Withdrawl amount:' '\\n'))\par
                print('Please take your Cash from the slot' '\\n')\par
                print('\\n''Please choose your next transaction: \\n')\par
                print('1 - Withdrawl \\n''2 - Deposit \\n''3 - Complaint' '\\n' '4 - Exit' '\\n')\par
                Option('\\n')\par
            elif(Option == 2):\par
                Deposit = (input('Enter Deposit amount:' '\\n'))\par
                print('Please insert your Deposit in the slot' '\\n')\par
                print('Please choose your next transaction:' '\\n')\par
                print('1 - Withdrawl \\n''2 - Deposit \\n''3 - Complaint' '\\n' '4 - Exit' '\\n')\par
                Option('\\n')\par
            elif(Option == 3):\par
                Complaint = str(input('Please detail your Complaint:' '\\n'))\par
                print('\\n''Thank you; your Complaint has been submitted' '\\n')\par
                print('\\n''Please choose your next transaction: \\n')\par
                print('1 - Withdrawl \\n''2 - Deposit \\n''3 - Complaint' '\\n' '4 - Exit' '\\n')\par
                Option('\\n')\par
            elif(Option == 4):\par
                print('Thank you for Banking with us.')\par
        elif(Option == 2):\par
            Deposit = (input('Enter Deposit amount:' '\\n'))\par
            print('Please insert your Deposit in the slot' '\\n')\par
            print('Please choose your next transaction:' '\\n')\par
            print('1 - Withdrawl \\n''2 - Deposit \\n''3 - Complaint' '\\n' '4 - Exit' '\\n')\par
            Option('\\n')\par
            if(Option == 1):\par
                Withdrawl = (input('Enter Withdrawl amount:' '\\n'))\par
                print('Please take your Cash from the slot' '\\n')\par
                print('\\n''Please choose your next transaction: \\n')\par
                print('1 - Withdrawl \\n''2 - Deposit \\n''3 - Complaint' '\\n' '4 - Exit' '\\n')\par
                Option('\\n')\par
            elif(Option == 2):\par
                Deposit = (input('Enter Deposit amount:' '\\n'))\par
                print('Please insert your Deposit in the slot' '\\n')\par
                print('Please choose your next transaction:' '\\n')\par
                print('1 - Withdrawl \\n''2 - Deposit \\n''3 - Complaint' '\\n' '4 - Exit' '\\n')\par
                Option('\\n')\par
            elif(Option == 3):\par
                Complaint = str(input('Please detail your Complaint:' '\\n'))\par
                print('\\n''Thank you; your Complaint has been submitted' '\\n')\par
                print('\\n''Please choose your next transaction: \\n')\par
                print('1 - Withdrawl \\n''2 - Deposit \\n''3 - Complaint' '\\n' '4 - Exit' '\\n')\par
                Option('\\n')\par
            elif(Option == 4):\par
                print('Thank you for Banking with us.')\par
        elif(Option == 3):\par
            Complaint = str(input('Please detail your Complaint:' '\\n'))\par
            print('\\n''Thank you; your Complaint has been submitted' '\\n')\par
            print('\\n''Please choose your next transaction: \\n')\par
            print('1 - Withdrawl \\n''2 - Deposit \\n''3 - Complaint' '\\n' '4 - Exit' '\\n')\par
            Option('\\n')\par
            if(Option == 1):\par
                Withdrawl = (input('Enter Withdrawl amount:' '\\n'))\par
                print('Please take your Cash from the slot' '\\n')\par
                print('\\n''Please choose your next transaction: \\n')\par
                print('1 - Withdrawl \\n''2 - Deposit \\n''3 - Complaint' '\\n' '4 - Exit' '\\n')\par
                Option('\\n')\par
            elif(Option == 2):\par
                Deposit = (input('Enter Deposit amount:' '\\n'))\par
                print('Please insert your Deposit in the slot' '\\n')\par
                print('Please choose your next transaction:' '\\n')\par
                print('1 - Withdrawl \\n''2 - Deposit \\n''3 - Complaint' '\\n' '4 - Exit' '\\n')\par
                Option('\\n')\par
            elif(Option == 3):\par
                Complaint = str(input('Please detail your Complaint:' '\\n'))\par
                print('\\n''Thank you; your Complaint has been submitted' '\\n')\par
                print('\\n''Please choose your next transaction: \\n')\par
                print('1 - Withdrawl \\n''2 - Deposit \\n''3 - Complaint' '\\n' '4 - Exit' '\\n')\par
                Option('\\n')\par
            elif(Option == 4):\par
                print('Thank you for Banking with us.')\par
        elif(Option == 4):\par
            print('Thank you for Banking with us.')\par
    else:\par
        print('Incorrect Password \\n''Please try again' '\\n')\par
else:\par
    print('Name not Authorized' '\\n''Please Try Again' '\\n')\par
}
