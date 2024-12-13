'''
Дано трехзначное число. Вывести число, полученное при
перестановке цифр десятков и единиц исходного числа (например, 123 перейдет в 132) '''

number = int

# проверка на корректность ввода числа
try:
    # Вводим число
    number = int(input("Введите 3 значное число"))
except ValueError:
  number = int(input("Введите 3 значное число"))
  

# проверка на корректность ввода 3 знаков
if len(str(number)) != 3:
  number = int(input("Введите 3 значное число"))

# делим на 100 на цело и получаем первое число (сотни)
frstNum = number // 100
# делим показывая остаток 0, потом делим на 10 на цело и получаем второе число (десятки)
scndNum = (number % 100) // 10
# аналогично. делим на 10, получаем остаток (десятки)
thrdNum = number % 10

# Получаем измененное число
swappedNumber = frstNum * 100 + thrdNum * 10 + scndNum
# Выводим измененное число
print("Переставленное число", swappedNumber)
