from select_friend import select_friend
import steganography.steganography
def send_message():
    friend_choice=select_friend()
#prepare a message
    original_message=raw_input('please enter image to hide messages:-')
    output_image=raw_input('please provide output to image:-')
    text=raw_input('enter your message:-')
    #encrypt the message
    steganography.steganography.Steganography.encode(original_message, output_image, text)
