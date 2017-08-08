print "               WELCOME TO SPY  \n                   CHAT"
spy_name = raw_input("Please provide your name here--")
if len(spy_name) > 0:
    spy_salutation = raw_input("What should we call you (MR or MISS)?-- ")
    spy_name = spy_salutation + " " + spy_name
    print"Welcome " + " " + spy_name + " glad to have you back with us ! "
    print "Alright"+ " "+spy_name+" " +"i want to know little more about you"
else:
    print"name cannot be blank"
#conatena"tion of salutation and name

