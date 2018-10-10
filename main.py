
from business.total_magic_numbers import TotalMagicNumbers

if __name__ == "__main__":
    number_of_inputs = int(input())
    input_data = []

    for count in range(0, number_of_inputs):
        number_init = int(input())
        number_end = int(input())
        input_data.append([
            number_init, number_end
        ])

    total = TotalMagicNumbers()
    result_magic_numbers = total.calculate(input_data)

    print(result_magic_numbers)