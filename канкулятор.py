
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = input("Выберите операцию из следующих =-*/%**//: ")

if num3 == "+":
    print(f"Ответ: {num1 + num2}")
elif num3 == "-":
    print(f"Ответ: {num1 - num2}")
elif num3 == "*":
    print(f"Ответ: {num1 * num2}")
elif num3 == "/":
    print(f"Ответ: {num1 / num2}")
elif num3 == "%":
    print(f"Ответ: {num1 % num2}")
elif num3 == "**":
    print(f"Ответ: {num1 ** num2}")
elif num3 == "//":
    print(f"Ответ: {num1 // num2}")
else:
    print("Данной операции нет в системе!")