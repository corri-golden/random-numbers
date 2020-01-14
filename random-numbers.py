import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1,6))
print(my_randoms)
# Generate a list of number 1..10
numbers_1_to_10 = list(range(1, 11))
print(numbers_1_to_10)
# Iterate from 1 to 10
for number in numbers_1_to_10:
    the_numbers_match = False
# Iterate your random number list here
    for i in my_randoms:
        if number == i:
            the_numbers_match = True
            print(f'my_randoms list contains {number}')
            break
    if the_numbers_match == False:
        print(f'my_randoms list does not contain {number}')
    the_numbers_match = False