def decimal_to_13(number):
    symbols = "0123456789ABC"

    if number == 0:
        return "0"
    
    result = ""
    is_negative = number < 0
    number = abs(number)

    while number > 0:
        remainder = number % 13
        result = symbols[remainder] + result
        number //= 13

    if is_negative:
        result = "-" + result
    
    return result

try:
    decimal_number = int(input("Введите десятичное число: "))
    print(f"Число {decimal_number} в системе счисления 13: {decimal_to_13(decimal_number)}")
except ValueError:
    print("Введите корректное целое число.")