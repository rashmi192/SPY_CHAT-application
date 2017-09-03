# import statements
from spy_details import spy #import spy details from spy_details
from start_chat import start_chat   #import start_chat will provide options to start your chat
print "               WELCOME TO SPY  \n                   CHAT"
while True:
    question = "Do you want to continue as " + spy['salutation'] + " " + spy['name'] + " (Y/N): " #value is stored in variable 'question'
    existing=raw_input(question)    #question as to continue as default user or new user

# validating users input

    if (existing.upper() == "Y") :  # user wants to continue as default user.

        spy_name = spy['salutation'] + " " + spy['name']    # concatination of salutation and name of spy.
        start_chat(spy['name'], spy['age'], spy['rating'], spy['is_online'])    # starting chat application

    elif (existing.upper() == "N"):    # user wants to continue as new user
        while True:         #loop is used until condition is fullfiled
            spy["name"] = raw_input("Enter your name here:- ")
            if len(spy['name']) > 0:       # check whether spy has input something or not
                spy['salutation'] = raw_input("What should we call you (Mr or Miss) ?: ")   #asking salutation
                break
            else:
                print'Name cannot be blank!'
        while True:
            try:                                                #asking user age
                spy['age'] = int(raw_input("Enter your age ? ")) # converting users input to integer (typecasting)
                spy['name'] = spy['salutation'] + " " + spy['name']  # concatination of salutation and name of spy. nd restoring in spy_name
                break
            except ValueError:
                    print"Your age is not valid !Please enter valid age ."  #exception handling is used because of run time error

        while True:
            try:
                spy['rating'] = float(raw_input("What is your spy rating?"))       #asking users rating
                if spy['rating'] > 4.5:                                             #using if else condition to evaluate users rating
                    print 'Excellent!'
                elif spy['rating'] > 3.5 and spy['rating'] <= 4.5:
                    print 'You are one of the good ones.'
                elif spy['rating'] >= 2.5 and spy['rating'] <= 3.5:
                    print 'You can do better'
                else:
                    print 'We can always use somebody to help in the office.'

                    # converting users input to float (typecasting)
            except ValueError:
                print 'Invalid Rating.'
                # starting chat application.
            spy['is_online'] = True
            start_chat(spy['name'], spy['age'], spy['rating'], spy['is_online'])    #starting chat applicaton
            break
        break

    else:
            print 'You entered wrong choice!'



