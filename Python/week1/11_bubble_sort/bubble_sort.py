import random
from datetime import datetime

x = random.sample(xrange(10000), 100)
i=0
j=(i+1)

start_time = datetime.now()

print x

def sort(x):
        for i in range (0,len(x)-1):
            for j in range (0, len(x)-1):
                if x[j]>x[j+1]:
                    x[j], x[j+1] = x[j+1], x[j]
                    print x

print sort(x)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
