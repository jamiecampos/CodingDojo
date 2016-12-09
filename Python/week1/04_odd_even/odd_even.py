#Create a function that counts from 1 to 2000. As it loops through each number,
#have your program generate the number and specify whether it's an odd or even
#number. Your program output should look like below:

#Number is 1.  This is an odd number.
#Number is 2.  This is an even number.
#Number is 3.  This is an odd number.
#...
#Number is 2000.  This is an even number.


def odd_even():
    for num in range(1, 2001):
        if (num % 2 == 0):
            print "Number is " + str(num) + ". This is an even number."
        else:
            print "Number is " + str(num) + ". This is an odd number."

print odd_even()
