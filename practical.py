# # Введення пін-кода (3 спроби)
# # Через while
# pin = '0123'
# n = 0
# max_tries = 3

# while n < max_tries:

#     user_pin = input('Enter your pin: ')

#     if len(user_pin) >= 4:
#         if pin == user_pin:
            
#             amount = input('How much: ')

#             if amount > 0:

#                 print(f'Take your {amount}')
#                 break

#         else:

#             print('Sorry, wrong pin. Try again please!')
#             print(f'You have {max_tries - n - 1} tries.')
#             n += 1

#     else:

#         print('Pin should be 4 or more digits.')
#         print(f'You have {max_tries - n - 1} tries.')
#         n += 1

# print('Good bye!')

# # Через for
# pin = '0123'
# for i in range(3):   
#     user_pin = input('Enter your pin: ')
#     if len(user_pin) == 4 or len(user_pin) == 6:
#         if pin == user_pin:
#             print("Here's your money")
#             break
#         else:
#             print('Sorry, wrong pin. Try again please!')
#     else:
#         print('Pin should be 4 or 6 digits.')
# print('Good bye!')


## Перевірка чи чичсло є поліндромом (зліва направа і зправа на ліво читається однаково)
num = int(input: )

n1 = num // 100
n2 = num % 10

if n1 == n2

## Перевірка чи одинакові цифри
num = input("Number: ")

if len(num) != 3:
    print ('Pleas enter 3 number')
else:
    n0 = int(num[0])
    n1 = int(num[1])
    n2 = int(num[2])

    if n0 != n2 and n1 != n2 and n1 != n0:
        print('Усі цифри різні')

    if (n0 == n2 or n1 == n2 or n1 == n0) and not (n0 == n1 and n0 == n2):
        print('Є тільки дві одинакові цифри')



