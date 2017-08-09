#import statements
from spy_details import spy_name, spy_salutation, spy_age, spy_rating
from start_chat import start_chat
print "               WELCOME TO SPY  \n                   CHAT"
question="Do you want to continue as" +" "+ spy_salutation + " " + spy_name + " " +":-Y/N=="
existing=raw_input(question)
if existing=='Y' or existing=='y':
    start_chat(spy_name, spy_age, spy_rating)
elif existing=='N'or existing=='n':
        if len(spy_name) > 0:
            spy_age = 0  # integer
            spy_rating = 0.0  # float
            spy_is_online = False  # boolean
            spy_name = raw_input("Please provide your name here--")  # input
            spy_salutation = raw_input("What should we call you (MR,MISS or MRS)?-- ")
            spy_name = "%s %s" % (spy_salutation, spy_name)  # concatenation#reassignment
            spy_age = int(raw_input("Please enter your age :-"))
            #spy age condition with and operator
            spy_rating = float(raw_input("Please enter your spy rating:-"));
            if spy_rating == 5.0:
                print"your rating is excellent..."
            elif 3.5 < spy_rating < 4.5:
                print"good rating.."
            else:
                print "ok ratings...."

            print"Welcome %s" % (spy_name), "glad to have you with us"
            print"Authentication Complete %s your Age is %d, and Rating is %f" % (spy_name, spy_age, spy_rating)
        else:
            print"SORRY,name cannot be blank"  # identation should be after:
        # conatenation of salutation and name
        # error is displayed in two form key nd value
else:
        print"wrong choie.try again"

