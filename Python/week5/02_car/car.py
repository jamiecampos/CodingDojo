class Car(object):
    def __init__(self, price, speed, fuel, mileage, tax=0):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = tax
        if self.price > 10000:
            self.tax = self.price * .15
        else:
            self.tax = self.price * .12

    def display_all(self):
        print "This car has a price of $", self.price, "and a maximum speed of", self.speed, ". It has", self.mileage, "on it and the gas tank is", self.fuel, ". Taxes are $", int(self.tax), "."
        return self

Ford = Car(2000, '25mph', 'Full', '15mpg')
Honda = Car(2000, '5mph', 'Not Full', '105mpg')
Acura = Car(2000, '15mph', 'Kind of Full', '95mpg')
Hyundai = Car(2000, '25mph', 'Full', '25mpg')
Chevy = Car(2000, '45mph', 'Empty', '25mpg')
GM = Car(20000000, '35mph', 'Empty', '15mpg')

Ford.display_all()
