import random
from datetime import datetime

x = random.sample(xrange(10000), 100)

start_time = datetime.now()

print x

def sort(x):
    min_index = 0
    max_index = 0
    num = 0
    while num<(len(x)/2):
        for i in range (num,len(x)-num):
            if x[i]>x[max_index]:
                max_index = i
            if x[i]<x[min_index]:
                min_index = i
        print min_index, max_index
        x[num], x[min_index] = x[min_index], x[num]
        x[len(x)-1-num], x[max_index] = x[max_index], x[len(x)-1-num]
        print x
        num += 1

print sort(x)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
