try:
    number_10 = float(input("Введите десятичное число (целое): "))
    if number_10.is_integer():
        number_10 = int(number_10)
        number_2 = bin(number_10)[2:]
        number_8 = oct(number_10)[2:]
        print(f"Двоичное представление: {number_2}")
        print(f"Восьмеричное представление: {number_8}")
    else:
        print("Ошибка: введено дробное число. Введите целое число.")
except ValueError:
    print("Ошибка: введено некоректное значение. Введите целое число.")