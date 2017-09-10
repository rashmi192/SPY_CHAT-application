#import statements
from spy_details import Spy,friends
from termcolor import colored
from spy_details import spy
#FUNCTION FOR ADDING A FRIEND
def add_friend():
    # Using the class spy
    new_friend = Spy(" ", " ", 0, 0.0)
    while True:
        new_friend.name = raw_input("Please add your friend's name:- ")
        if len(new_friend.name)>0:
            while True:
                new_friend.salutation = raw_input("Are they Mr. or Ms. ?:- ")
                if len(new_friend.salutation)>0:
                    if (new_friend.salutation == 'ms.' or new_friend.salutation == 'Ms.' or new_friend.salutation == "Mr." or new_friend.salutation == "mr."):
                        # ask for the age of the friend
                        while True:
                            new_friend.age = raw_input("Age?:- ")

                            # Type casting to integer
                            if len(new_friend.age) > 0:
                                new_friend.age = int(new_friend.age)
                                if 18 < new_friend.age < 50:
                                        # After the conditions are satisfied the friend will be added
                                        friends.append(new_friend)
                                        print(colored('FRIEND ADDED!', "magenta"))

                                else:
                                        print (colored("Sorry but your age is not valid for spy!", 'red'))
                                        print(colored("       THANK YOU!       ", 'yellow'))
                                        exit()
                                return len(friends)
                                        #application will terminate
                                                # The no of friends the spy has will be returned.
                                             # The no of friends the spy has will be returned.
                            else:
                                    print (colored("Sorry but age cannot be blank!", 'red'))



                        # The no of friends the spy has will be returned.
                    else:
                        print(colored('Please enter valid salutation!', 'red'))
                else:
                    print(colored('Salutation cannot be blank!','red'))
        else:
            print(colored('Name cannot be blank!','red'))
            return len(friends)