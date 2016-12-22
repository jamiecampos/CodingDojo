class MathDojo(object):
    def __init__(self, result = 0):
        self.result = result

    def add(self, *args):
        for arg in args:
            self.result += arg
        return self

    def subtract(self, *args):
        for arg in args:
            self.result -= arg
        return self

md = MathDojo()
print md.add(2).add(2, 5).subtract(3, 2).result
