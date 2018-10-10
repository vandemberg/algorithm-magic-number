import math

class MagicNumber(object):
    def countMagicsNumbers(self, init, end):
        sum = 0

        for number in range(init, end + 1):
            if(self.isMagicNumber(number)):
                sum += 1

        return sum
    
    def isMagicNumber(self, number):
        if( self.__haveSquare(number) ):
            return True
        
        return False
    
    def __isPrime(self, number):
        number = abs( int(number) )
        
        if number < 2:
            return False

        if number == 2: 
            return True    

        if not number & 1: 
            return False

        for x in range(3, int(number ** 0.5) + 1, 2):
            if number % x == 0:
                return False

        return True
    
    def __haveSquare(self, number):
        
        if ( math.sqrt(number) - int(math.sqrt(number)) ):
            return False

        number = math.sqrt(number)

        if not self.__isPrime(number):
            return False        
        
        return True