
from business.count_number_magic import CountMagicNumber

if __name__ == "__main__":
    number_of_inputs = int(input("Quantidade de valores inseridos: "))
    sum_magic_numbers = 0
    count = 0
    magic_number = MagicNumber()

    for count in range(0, number_of_inputs):
        number_init = int(input("Valor incial: "))
        number_end = int(input("Valor final: "))

        sum_magic_numbers += magic_number.countMagicsNumbers(number_init, number_end)
    
    print(sum_magic_numbers)