class MathDojo(object):
    def __init__(self, result = 0):
        self.result = result

    def add(self, *args):
        for arg in args:
            if type(arg) == int:
                self.result += arg
            elif type(arg) == list:
                self.result += sum(arg)
            elif type(arg) == tuple:
                self.result += sum(arg)
        return self

    def subtract(self, *args):
        for arg in args:
            if type(arg) == int:
                self.result -= arg
            elif type(arg) == list:
                self.result -= sum(arg)
            elif type(arg) == tuple:
                self.result += sum(arg)
        return self

md = MathDojo()
print md.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
