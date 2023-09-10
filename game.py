SIZE_N = 5
SIZE_M = 5

char_x = 1
char_y = 1

exit_x = 4
exit_y = 4



while True:

    world_map = ''

    for j in range(SIZE_M):
        row = '|'

        for i in range(SIZE_N):
        
            if char_x == i and char_y == j:
                row += 'X|'
            elif exit_x == i and exit_y == j:
                row += 'O|'
            else:
                row += ' |'

        world_map += f'{row}\n'
    
    print(world_map)

    direction = input('Enter direction (u / d / l / r): ')

    if direction == 'u' and char_y > 0:
        char_y -= 1
    elif direction == 'd' and char_y < SIZE_M - 1:
        char_y += 1
    elif direction == 'l' and char_x > 0:
        char_x -= 1
    elif direction == 'r' and char_x < SIZE_N - 1:
        char_x += 1
    
  

