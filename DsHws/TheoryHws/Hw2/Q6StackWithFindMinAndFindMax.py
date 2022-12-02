class sStack():
    stack = []
    min = 0
    max = 0

    def __init__(self):
        pass

    def push(self, value):
        if len(self.stack) == 0 :
            self.min , self.max = value,value
            self.stack.append(value)
            return
        if value > self.max:
            self.max, value = value, value + (value - self.max)
        if value < self.min or len(self.stack) == 0 :
            self.min , value = value , value - (self.min - value)
        self.stack.append(value)

    def pop(self):
        value = self.stack.pop()
        if len(self.stack) == 0 :
            self.min , self.max = 0, 0
            return value
        if value > self.max :
            value , self.max = self.max , self.max - (value - self.max)
        if value < self.min :
            value , self.min = self.min , self.min + (self.min - value)
        return value


    def findMax(self):
        return self.max

    def findMin(self):
        return self.min


def createStack():
    return sStack()
