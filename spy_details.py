# Importing datetime to display the chat time and date
from datetime import datetime

# created class for spy
class Spy:

    def __init__(self, name, salutation, age, rating):
        # Initializing the values
        self.name = name #name of the spy
        self.salutation = salutation #salutation of the spy
        self.age = age #age of the spy
        self.rating = rating #rating of the spy
        self.is_online = True #is online
        self.chats = [] #lists for saving the conversations
        self.current_status_message = None #initialising nothing in current status
        # Count the number of words
        self.count = 0

# created class for chat_messages
class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message  #for messages
        self.time = datetime.now()  #for date and time
        self.sent_by_me = sent_by_me    #either true or false

spy = Spy('Rashmi Pandey', 'Ms.', 20, 5)  #predefined user for the beginning

#added some friends just to save time .....no need of entering new friend data again and again
friend_one = Spy('Ravi', 'Mr.', 27, 4)
friend_two = Spy('Suraj', 'Mr.', 21, 5)
friend_three = Spy('Ruhi', 'Ms.', 27 , 5)

# List of friends
friends = [friend_one, friend_two, friend_three]