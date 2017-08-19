from select_friend import select_friend
from steganography.steganography import Steganography
def read_message():
    #choose friend from list
    sender=select_friend()
    encrypted_image=raw_input('provide encrypted image:')
    secret_message=Steganography.decode(encrypted_image)
    print secret_message