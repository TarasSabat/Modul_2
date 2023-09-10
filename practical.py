# # Введення пін-кода (3 спроби)
# # Через while
pin = '0123'
n = 0
max_tries = 3

while n < max_tries:

    user_pin = input('Enter your pin: ')

    if len(user_pin) >= 4:
        if pin == user_pin:
            
            amount = input('How much: ')

            if amount > 0:

                print(f'Take your {amount}')
                break

        else:

            print('Sorry, wrong pin. Try again please!')
            print(f'You have {max_tries - n - 1} tries.')
            n += 1

    else:

        print('Pin should be 4 or more digits.')
        print(f'You have {max_tries - n - 1} tries.')
        n += 1

print('Good bye!')

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

