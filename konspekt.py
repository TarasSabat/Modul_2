# name = input("What is your name? ")
# print(f"Hello {name}")

# # Умовне виконання
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

# # Булева алгебра
# name = "Taras"
# age = 22
# has_driver_licence = True

# if name and age >= 18 and has_driver_licence:
#     print(f"User {name} can rent a car")

# # Тернарні операції
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

