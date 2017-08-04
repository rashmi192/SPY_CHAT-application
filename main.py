print "               WELCOME TO SPY  \n                   CHAT"
spy_name=raw_input("Please provide your name here--")
if len(spy_name)>0:

    spy_salutation = raw_input("What should we call you (MR or MISS)?-- ")
if len(spy_salutation) > 0:

    print"Welcome " + spy_salutation + " " + spy_name + " glad to have you back with us ! "
else:
    print "Sorry,name cannot be blank!"


#conatenation of salutation and name

#spy_name =spy_salutation + " " + spy_name (this is called reassignment)
