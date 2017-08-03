print("\nCALCULATOR:-")
a=input("enter your choice :- 1.addition \n 2.subtraction \n 3.multiplication \n 4.division\n")
b=input("enter the  first value:-")
c=input("enter the second value:-")
if a==1:
    print "Addition of two number is :-"+ `b+c`
elif a==2:
    print "Subtraction of two number is :-"+ `b-c`

elif a==3:
     print "Multiplication of two number is :-"+ `b*c`

elif a==4:
     print "Division of two number is :-"+ `b/c`

else:
     print "wrong option"