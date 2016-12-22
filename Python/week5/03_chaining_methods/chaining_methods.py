class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print "Price: ", self.price, ", Maximum Speed: ", self.max_speed, ", Total Miles: ", self.miles
        return self
    def ride(self):
        print "Riding"
        self.miles = self.miles + 10
        return self
    def reverse(self):
        print "Reversing"
        self.miles = self.miles - 5
        if self.miles < 0:
            self.miles = 0
        return self

mongoose = Bike(100.00, '15mph')
schwinn = Bike(250.00, '25mph')
huffy = Bike(6.00, '2mph')

mongoose.ride().ride().ride().reverse().displayInfo()
