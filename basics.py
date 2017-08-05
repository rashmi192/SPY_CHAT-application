list = [ 'abcd', 123 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list          # Prints complete list
print list[0]       # Prints first element of the list
print list[1:3]     # Prints elements starting from 2nd till 3rd
print list[2:]      # Prints elements starting from 3rd element
print tinylist * 2  # Prints list two times
print list + tinylist # Prints concatenated lists


print("\nCALCULATOR:-")

a=int(raw_input("enter your choice :- 1.addition \n 2.subtraction \n 3.multiplication \n 4.division\n"))
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





