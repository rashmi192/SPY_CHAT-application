#used import statements
import matplotlib
import matplotlib.pyplot as plt
from spy_details import spy,Spy
from start_chat import start_chat
#used color to print colored lines and imported from library
from termcolor import colored
font = {'family': 'sans-serif',
        'weight': 'bold',
        'size' : 22}

print colored(" -----------------------WELCOME TO SPY CHAT -----------------------",'magenta')
while True:
    #question as to continue as default user or new user
    question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)?:- " #concatenation of name and salutation is done
    # value is stored in variable 'question
    existing = raw_input(question)
    # validating users input
    # if the user chooses the default spy
    if existing.upper() == "Y":
        # start the chat function is called
        start_chat(spy)
    # the user wants to add a new user in spy chat
    elif existing.upper() == "N":
        # declared variables using a class
        spy = Spy(" ", " ", 0, 0.0)
        # loop is used until condition is fullfiled
        while True:
            # asking users name
            spy.name = raw_input("Enter your name here:- ")

            # Check if the name is entered or not
            if len(spy.name) > 0 and spy.name.isdigit() == False:
                # ask for the salutation
                while True:
                    spy.salutation = raw_input("What should we call you Mr. or Ms.?:-")

                    # check if salutation is entered correct or not
                    if (spy.salutation == 'ms.' or spy.salutation == 'Ms.' or spy.salutation == "Mr." or spy.salutation == "mr."):

                        # Ask for the age of the spy
                        while True:
                            spy.age = raw_input("Please enter your age:-")

                            #when age of spy is not blank ,greater than 0
                            if len(spy.age) > 0:
                                # raw input always gives a string to typecast age to int.
                                spy.age = int(spy.age)
                                #when age of spy is between 18 and 50
                                if 18 < spy.age < 50:
                                   # Ask for spy_rating
                                    while True:
                                        spy.rating = raw_input("Please enter your spy rating:- ")
                                        #when rating is greater than 0 then
                                        if len(spy.rating) > 0:
                                            # raw input always gives a string to typecast rating to float.
                                            spy.rating = float(spy.rating)

                                            # conditions to pass comments according to the spy_rating.
                                            if spy.rating > 4.5:
                                            # using if else condition to evaluate users rating
                                                print colored('Excellent!','green')
                                            elif spy.rating > 3.5 and spy.rating <= 4.5:
                                                print colored('You are one of the good ones.','green')
                                            elif spy.rating >= 2.5 and spy.rating <= 3.5:
                                                print colored('You can do better','green')
                                            else:
                                                print colored('Your rating is not valid','red')

                                            # Make the spy come online
                                            spy.is_online = True

                                            # Call the start_chat function to start(the function will authenticate the user)
                                            start_chat(spy)

                                        # If spy rating is not entered
                                        else:
                                            print (colored("Enter a valid spy rating!",'red'))

                                # valid age is not entered or less than 18 or greater than 50
                                else:
                                    print (colored("Sorry but your age is not valid for spy!", 'red'))
                                    print(colored("       THANK YOU!       ", 'yellow'))
                                    exit()  #application will terminate
                            else:
                                print(colored("Age cannot be blank!", 'red'))
                    # the salutation is not entered
                    else:
                        print(colored("Please enter a valid salutation!",'red'))


            # the name is not entered
            else:
                print(colored("Name cannot be blank,Please enter valid name!",'red'))
    #when correctly not choosed  option
    else:
        print(colored("Please reply with a yes(Y) or no(N)!", 'red'))

