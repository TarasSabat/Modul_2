'''
На технічній співбесіді претенденти на посаду одержують оцінку за тест. 
У наступний тур співбесіди проходять кандидати, які склали тест на 83 бали включно або вище. 
Реалізуйте оператор контролю виконання так, щоб він привласнив логічній змінній is_next значення True, 
якщо кількість набраних балів буде більшою або дорівнює 83. 
В іншому випадку значення змінної дорівнює False.
'''
# is_next = 83
# num = int(input("Enter the number of points: "))
# if num >= is_next:
#     is_next = True
#     print('True')
# else:
#     is_next = False
#     print('False')

'''
У нас є три логічні змінні.
Перша визначає статус користувача is_active, яка дорівнює True або False.
Друга is_admin визначає, чи є у користувача права адміністратора теж булевого типу.
Третя is_permission — чи дозволено доступ, теж булевого типу.
Приведіть змінні is_active, is_admin та is_permission до булевого вигляду.
Надайте змінній access значення, яке покаже, чи є доступ у користувача. Використовуйте логічні оператори.
Адміністратор завжди має доступ, незалежно від значень змінних is_permission та is_active.
Користувач має доступ, тільки якщо is_permission дорівнює True та is_active також дорівнює True.
'''
# is_active = (input("Is the user active? "))
# is_admin = (input("Is the user administrator? "))
# is_permission = (input("Does the user have access? "))

# is_active = bool(is_active) 
# is_admin = bool(is_admin)
# is_permission = bool(is_permission)

# access = is_active and is_permission or is_admin
'''
Як відомо, зазвичай розробників заведено поділяти на три категорії: 
Джун (Junior) & mdash; молодший спеціаліст, Мідл ( Middle) — основний розробник у компанії та Сеньйор 
(Senior) — старший розробник. Орієнтовно можна вважати, що до 1 року роботи включно — це Джуніор, 
понад 5 років — це Сеньйор розробник, а від одного року до 5 включно — мідл.
Є змінна work_experience, що визначає стаж роботи програміста. Залежно від стажу роботи, 
присвоїти змінній developer_type значення "Junior", "Middle" або "Senior". Використовуйте, 
якщо необхідно, булеві оператори or та and під час перевірок.
'''
# work_experience = float(input("Enter your full work experience in years: "))

# if 1 < work_experience <= 5:
#     developer_type = "Middle"
# elif work_experience <= 1 :
#     developer_type = "Junior"
# else:
#     developer_type = "Senior"
# print(developer_type)
'''
Перепишіть приклад із теорії, але для додатного числа перевіряйте — парне воно чи ні. 
Таким чином після перевірок змінна result повинна містити одне з чотирьох значень:
"Positive even number"
"Positive odd number"
"Negative number"
"It is zero"
Підказка: перевірка на парність виконується порівнянням залишку від поділу на 2 з 0 або 1. 
Нагадаємо, залишок від ділення можна отримати після операції %
'''
# num = int(input("Enter a number: "))

# if num > 0:
#     if num % 2 == 0:
#         result = "Positive even number"
#     else:
#         result = "Positive odd number"
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"

# print(result)

'''

