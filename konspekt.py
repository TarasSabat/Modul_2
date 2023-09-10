# name = input("What is your name? ")
# print(f"Hello {name}")

# # Умовне виконання (Conditional statement)
# if bool(True):   # завжди bool
#     print('Hello')

# age = input("How old are you? ")
# if int(age) >= 18:
#     print("You are adult already.")
# else:
#     print("You are infant yet.")

# # Синтаксис умовного виконання
# # Приклад 1
# a = input('Введіть число')
# a = float(a)
# if a > 0:
#     print('Число додатне')
# elif a < 0:
#     print("Число від'ємне")
# else:
#     print('Це число - нуль')

# # Приклад 2
# a = input('Введіть число')
# a = int(a)
# if a > 0:
#     print('Число додатне')
# elif a == 1:
#     print('Число дорівнює 1')
# else:
#     print("a <= 0")
# # В такому випадку код для умови a == 1 ніколи не виконається.


# # Для зручності у Python є механізм неявного приведення будь-якого типу до типу bool. 
# # Правила приведення до bool — інтуїтивні:
# # - число 0 приводиться до False (ціле, дробове або комплексне);
# money = 0
# if money:
#     print(f"You have {money} on your bank account")
# else:
#     print("You have no money and no debts")

# # - None приводиться до False;
# result = None
# if result:
#     print(result)
# else:
#     print("Result is None, do something")

# # -порожній контейнер (порожній рядок тощо) приводиться до False
# user_name = input("Enter your name: ")

# if user_name:
#     print(f"Hello {user_name}")
# else:
#     print("Hi Anonym!")

# # - все інше приводиться до True

# # Булева алгебра. Логічні оператори (Logical operators)
# name = "Taras"
# age = 22
# has_driver_licence = True

# if name and age >= 18 and has_driver_licence:
#     print(f"User {name} can rent a car")

# # Тернарні операції (Inline conditional statement)
# age = 23
# adult = True if age >= 18 else False
# print(adult)

# is_nice = True
# state = "nice" if is_nice else "not nice"

# # коротший варіант тернарного оператора
# some_data = None
# msg = some_data or "Не було повернено даних"

# # Блоки інструкцій
# x = int(input("X: "))
# y = int(input("Y: "))

# if x == 0:
#     print("X can`t be equal to zero")
#     x = int(input("X: "))

# result = y / x

# # Для виділення декілька рівнів вкладеності, додаючи ще 4 пробіли зліва для всіх інструкцій блоку:
# x = int(input("X: "))
# y = int(input("Y: "))

# if x == 0:
#     print("X can`t be equal to zero")
#     x = int(input("X: "))

#     if x == 0:
#         print("X can`t be equal to zero")
#         x = int(input("X: "))

#         if x == 0:
#             print("X can`t be equal to zero")
#             x = int(input("X: "))

# result = y / x

# # Приклад вкладеності для визначення чвертей для координатної площини.
# if x >= 0:
#     if y >= 0:               # x > 0, y > 0
#         print("Перша чверть")
#     else:                    # x > 0, y < 0
#         print("Четверта чверть")
# else:
#     if y >= 0:               # x < 0, y > 0
#         print("Друга чверть")
#     else:                    # x < 0, y < 0
#         print("Третя чверть")

# # Цикл for (для)
# fruit = 'apple'
# for char in fruit:
#     print(char)

# # Цикл while (поки)
# while True: 
#     print('Hello')  # безскінчений цикл

# a = 1
# while a <= 5:
#     print(a)
#     a = a + 1     # аналогічно a += 1

# # «Нескінченні цикли» та break
# a = 0
# while True:
#     print(a)
#     if a >= 20:
#         break
#     a = a + 1

# # Наприклад echo скрипт, який виводить в консоль те, що ви введете, доки ви не введете exit:
# while True:
#     user_input = input()
#     print(user_input)
#     if user_input == "exit":
#         break

# # Завершення ітерації за допомогою continue
# a = 0
# while a < 6:
#     a = a + 1
#     if not a % 2:
#         continue
#     print(a)

# # Оператори continue та break працюють тільки всередині одного циклу. 
# # В ситуації вкладених циклів немає способу вийти з усіх циклів одразу.
# while True:
#     number = input("number = ")
#     number = int(number)
#     while True:
#         print(number)
#         number = number - 1
#         if number < 0:
#             break

# # Також використання continue або break поза циклом призводить до синтаксичної помилки.
# number = int(input("number = "))
# if number < 0:
#     break

# # Винятки
# val = 'a'
# try:
#     val = int(val)
# except ValueError:
#     print(f"val {val} is not a number")
# else:
#     print(val > 0)
# finally:
#     print("This will be printed anyway")

# # Механізм обробки винятків
# age = input("How old are you? ")
# try:
#     age = int(age)
#     if age >= 18:
#         print("You are adult.")
#     else:
#         print("You are infant")
# except ValueError:
#     print(f"{age} is not a number")

