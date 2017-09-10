#import statements
from select_friend import select_a_friend
from spy_details import ChatMessage,friends
from termcolor import colored
# import steganography from library
from steganography.steganography import Steganography
# Function to send a secret message
def send_a_message():
    # Select a friend to whom you want to send and receive msgs  with
    friend_choice = select_a_friend()

    # Select the image in which you want to write a secret message
    while True:
        original_image = raw_input("What is the name of the image?:- ")
        if len(original_image) >0:

            # the output path of the image where the message is stored
            while True:
                output_path = raw_input("Provide the name of the output image :- ")
                if len(output_path) > 0:
                    #write the secret message
                    while True:
                        text = raw_input("Enter your secret message:- ")
                        if len(text) > 0:
                            # The library steganography that helps to encode the message
                            Steganography.encode(original_image, output_path, text)

                            # The text message wil be stored in chat messages
                            new_chat = ChatMessage(text, True)

                            # Along with the name of the friend we add the message
                            friends[friend_choice].chats.append(new_chat)

                            # After the encoding is done the message is ready.
                            print(colored("Your secret message image is ready!", "cyan"))
                            #returning back to menu choice
                            return new_chat

                        else:
                            print(colored('Secret message cannot be blank!', 'red'))
                else:
                    print(colored('Output image cannot be blank!', 'red'))
        else:
            print(colored('Input Image cannot be blank!','red'))
