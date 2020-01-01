import os
import random
import time

num_range = (input('Enter a number of random numbers to generate: '))
while num_range.isnumeric() is False:
    print('You have to enter a number!')
    num_range = (input('Enter a number of random numbers to generate: '))

num_start = (input('Enter first number of range: '))
while num_start.isnumeric() is False:
    print('You have to enter a number!')
    num_start = (input('Enter first number of range: '))

num_end = (input('Enter last number of range: '))
while num_end.isnumeric() is False:
    print('You have to enter a number!')
    num_end = (input('nter last number of range: '))

def gen_numbs(start, end):
    file_name = (input("Enter the name of a file: ") + '.txt')
    numbers_file = open(file_name, "w+")
    count = 0


    for i in range(int(num_range)):
        count += 1
        ran_num = str(random.randint(int(start), int(end)))
        numbers_file.write(f'{count}. -- {ran_num}\n')
        percent = (count / int(num_range)) * 100
        def print_perc():
            print(f'{int(percent)}% - ', end='')

        if percent == 10:
            print_perc()
        elif percent == 20:
            print_perc()
        elif percent == 30:
            print_perc()
        elif percent == 40:
            print_perc()
        elif percent == 50:
            print_perc()
        elif percent == 60:
            print_perc()
        elif percent == 70:
            print_perc()
        elif percent == 80:
            print_perc()
        elif percent == 90:
            print_perc()
        elif percent == 100:
            print(f'{int(percent)}%')

    print('Your file is generated at ' + os.path.realpath(numbers_file.name))


    numbers_file.close()
gen_numbs(num_start, num_end)


time.sleep(100)