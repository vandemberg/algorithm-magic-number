
from business.calculate_magic_numbers import CalculateMagicNumbers

class TotalMagicNumbers(object):
    
    def __init__(self):
        self.magicNumbers = CalculateMagicNumbers()

    def calculate(self, data = []):

        result = 0

        for numbers in data:
            init = numbers[0]
            end = numbers[1]

            result += self.magicNumbers.calculate(init, end)
        
        return result



