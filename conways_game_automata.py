# print('{WELCOME TO CONWAYS GAME OF LIFE AUTOMATA}'.center(100, '~'))
# import random
# import time
# time.sleep(3)
# main_list = []
# x = 0
# while x <= 24:
#     if (random.randint(0, 1)) == 1:
#         main_list += ['#']
#     else:
#         main_list += [' ']
#     x += 1
# print(f'{main_list[0:5]}\n'
#       f'{main_list[5:10]}\n'
#       f'{main_list[10:15]}\n'
#       f'{main_list[15:20]}\n'
#       f'{main_list[20:25]}')
# copied_list = main_list.copy()
# while True:
#     x = 0
#     while x <= 24:
#         left = 0
#         right = 0
#         above = 0
#         below = 0
#         if x != 0 and x != 5 and x != 10 and x != 15 and x != 20:
#             left += (x - 1)
#         if x != 4 and x != 9 and x != 14 and x != 19 and x != 24:
#             right = (x + 1)
#         if x > 4:
#             above = (x - 5)
#         if x < 20:
#             below = (x + 5)
#         neighbouring_live_cells = 0
#         y = 0
#         while y < 1:
#             if left != 0:
#                 if copied_list[left] == '#':
#                     neighbouring_live_cells += 1
#             if right != 0:
#                 if copied_list [right] == '#':
#                     neighbouring_live_cells += 1
#             if above != 0:
#                 if copied_list[above] == '#':
#                     neighbouring_live_cells += 1
#             if below != 0:
#                 if copied_list[below] == '#':
#                     neighbouring_live_cells += 1
#             y += 1
#         if neighbouring_live_cells >= 3:
#             main_list[x] = '#'
#         elif neighbouring_live_cells <= 1:
#             main_list[x] = ' '
#         x += 1
#     if main_list == copied_list:
#         print()
#         print()
#         print('Same Pattern Continues'.center(100, '-'))
#         break
#     copied_list = main_list.copy()
#     time.sleep(2)
#     print()
#     print()
#     print(f'{main_list[0:5]}\n'
#           f'{main_list[5:10]}\n'
#           f'{main_list[10:15]}\n'
#           f'{main_list[15:20]}\n'
#           f'{main_list[20:25]}')
import random
import time
print('CONWAYS GAME AUTOMATA'.center(100, '~'))
time.sleep(0.5)
print('⬇ INSTRUCTIONS ⬇ \n'.center(100))
time.sleep(0.5)
print('1 : Cell having 2 neighbours remains same.')
time.sleep(0.5)
print('2 : Cell having more than 2 neighbours become alive.')
time.sleep(0.5)
print('3 : Cell having less than 2 neighbours become dead.')
time.sleep(0.5)
print('4 : ⚪ = ALive cell.')
time.sleep(0.5)
print('5 : ⚫ = Dead cell.')
time.sleep(0.5)
input('press ENTER to continue...')
main_list = []
x = 0
while x < 25:
    random_value = random.randint(0, 1)
    if random_value == 1:
        main_list += ['⚪']
    else:
        main_list += ['⚫']
    x += 1
print('\n1️⃣ pattern...\n')
print(f'{main_list[0:5]}\n'
      f'{main_list[5:10]}\n'
      f'{main_list[10:15]}\n'
      f'{main_list[15:20]}\n'
      f'{main_list[20:25]}\n')
# copied_list = main_list.copy()
n = {2: "2️⃣", 3: '3️⃣', 4: '4️⃣'}
j = 2
while True:
    copied_list = main_list.copy()
    input(f'{n.get(j, "Next")} pattern...'
          f'\n')
    y = 0
    while y < 25:
        left = 0
        right = 0
        above = 0
        below = 0
        if y != 0 and y != 5 and y != 10 and y != 15 and y != 20:
            if copied_list[y - 1] == '⚪':
                left += 1
        if y != 24 and y != 9 and y != 14 and y != 19 and y != 4:
            if copied_list[y + 1] == '⚪':
                right += 1
        if y > 4:
            if copied_list[y - 5] == '⚪':
                above += 1
        if y < 20:
            if copied_list[y + 5] == '⚪':
                below += 1
        neighbouring_cells = left + right + above + below
        if neighbouring_cells <= 1:
            main_list[y] = '⚫'
        elif neighbouring_cells >= 3:
            main_list[y] = '⚪'
        y += 1
    j += 1
    print(f'{main_list[0:5]}\n'
          f'{main_list[5:10]}\n'
          f'{main_list[10:15]}\n'
          f'{main_list[15:20]}\n'
          f'{main_list[20:25]}\n')
    if main_list == copied_list:
        print('Same pattern continues...')
        break
