import random
from datetime import datetime

x = [5,4,3,2,1]

start_time = datetime.now()

print x

def sort(x):
    for right in range (1, len(x)):
        left = (right-1)
        print "for loop"
        while right > 0 and x[right] < x[left]:
            print "right=", right, "statement=", x[right], " < " , x[left]
            print x[right] < x[left]
            x[left], x[right] = x[right], x[left]
            right -= 1
            left -= 1
        else:
            right += 1
            print x

print sort(x)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
