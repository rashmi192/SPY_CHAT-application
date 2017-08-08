print "               WELCOME TO SPY  \n                   CHAT"
spy_name = raw_input("Please provide your name here--")#input
if len(spy_name) > 0:
    spy_age = 0  # integer
    spy_rating = 0.0  # float
    spy_is_online = False  # boolean
    spy_salutation = raw_input("What should we call you (MR,MISS or MRS)?-- ")
    spy_name = "%s %s"%(spy_salutation,spy_name)#concatenation#reassignment
    spy_age = int(raw_input("Please enter your age :-"))
    if spy_age>18 & spy_age<30:
        spy_rating=float(raw_input("Please enter your spy rating:-"));
        if spy_rating==5.0:
            print"your rating is excellent..."
        elif 3.5 < spy_rating < 4.5:
            print"good rating.."
        else:
            print "ok ratings...."

    print"Welcome %s"%(spy_name),"glad to have you with us"
    print"Authentication Complete %s your Age is %d, and Rating is %f"%(spy_name,spy_age,spy_rating)

else:
    print"SORRY,name cannot be blank"#identation should be after:
#conatenation of salutation and name
#error is displayed in two form key nd value

