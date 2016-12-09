import random
from datetime import datetime

x = random.sample(xrange(10000), 100)
i = 0
j = (i+1)

start_time = datetime.now()

print x

def sort(x):
        for i in range (0,len(x)/2):
            min_number = i
            for j in range (i+1, len(x)-TOP):
                if x[j] < x[min_number]:
                    min_number = j
				if x[j] > x[max_number]:
                    max_number = y
            if min_number != i:
                x[i], x[min_number] = x[min_number], x[i]
            if max_number != z:  (some kind of max swap here)
                x[z], x[max_number] = x[max_number], x[z]  (indexes are not right now)
			TOP=TOP+1 (to shorten the search range of the j loop)
                print x

print sort(x)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
