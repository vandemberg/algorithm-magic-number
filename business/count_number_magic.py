
from business.number_magic import MagicNumber

class CountMagicNumber(object):
    
    def __init__(self):
        self.magicNumber = MagicNumber()

    def calculate(self, data = []):
        for numbers in data:
            init = numbers[0]
            end = numbers[0]



