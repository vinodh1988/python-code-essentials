class NegativeError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return "{} is a negative number".format(self.value)

class DenominatorError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return "{} is greater than numerator and should not be".format(self.value)
