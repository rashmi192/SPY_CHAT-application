#Import statements is used to import from other files
from add_status import add_status
from add_friend import add_friend
from send_message import send_a_message
from read_chat import read_chat
from send_message_help import send_message_help
from read_message import read_message
from termcolor import colored

#function contains all the functions
def start_chat(spy):
    # updated variable
    #concatenation of name and salutation
    spy.name = spy.salutation + " " + spy.name
    # Age cannot be less than 18 or greater than 50
    if 18 < spy.age < 50:
        #all details from users is taken nd message is displayed  of authentication complete with his/her details

        print(colored("Authentication complete.",'green'))
        print(colored("Welcome " + str(spy.name), "green"))
        print(colored("Your age:" + str(spy.age), "green"))
        print(colored("Your rating:"+str(spy.rating), "green"))
        print(colored("Bravo!Proud to have you on board.", "yellow"))
        print(colored("THANK YOU FOR YOUR DETAILS!", 'yellow'))


        show_menu = True
        #infinite loop is used till condition is satisified
        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n" \
                           " 2. Add a friend \n 3. Send a secret message \n " \
                           "4. Read a secret message \n 5. Read Chats from a user \n" \
                           " 6. Close Application \n"
            #here are the options what we can do in our application send,read msg etc
            # Taking the input of the choice
            menu_choice = raw_input(colored(menu_choices, "blue"))

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    # Set your current status
                    spy.current_status_message = add_status()

                elif menu_choice == 2:
                    # Add a new friend
                    number_of_friends = add_friend()
                    print 'You have %d friends' % number_of_friends

                elif menu_choice == 3:
                    # Send a secret message
                    send_a_message()

                elif menu_choice == 4:
                    # Read the secret message sent by your friend
                    read_message()

                elif menu_choice == 5:
                    # Read the chat history
                    read_chat()

                elif menu_choice == 6:
                    # Close the app
                    exit()

                # When the user chooses other than the menu choices.
                else:
                    print(colored("That was a wrong choice.", 'red'))
                    exit()
                    #now it will terminate
