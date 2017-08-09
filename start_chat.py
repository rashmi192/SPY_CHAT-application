#start chat function
def start_chat(spy_name,spy_age,spy_rating):
    show_menu=True
    menu_choices = "What do you want to do? \n 1. Add a status update\n"
    result=raw_input("menu_choices")

    #validating user input
    if(result==1):
        pass
    elif(result==2):
        show_menu=False
    else:
        print'wrong choice'