#Create a function called 'multiply' that reads each value in the list
#(e.g. a = [2, 4, 10, 16]) and returns a list where each value has been
#multiplied by 5. The function should multiply each value in the list by the
#second argument. For example, let's say:

#a = [2,4,10,16]
#Then:
#b = multiply(a, 5)
#print b
#Should print [10, 20, 50, 80 ].

a = [2,4,10,16]
b = 5

def multiply(arr,mult):
    for i in range(len(a)):
        arr[i] = arr[i]*mult
    return arr

print multiply(a,b)
