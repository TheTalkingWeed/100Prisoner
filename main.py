import random

freed = False
number = 0
numberOfPicks = 0
ind = 0



numbers = []
for j in range(100):
    numbers.append(j)


random.shuffle(numbers)


while number < 100:
    ind = number
    numberOfPicks = 0
    while numberOfPicks<50:
        if numbers[ind] == number:
            freed = True
            break 
        ind = numbers[ind]
        numberOfPicks += 1
    if freed == False:
        print('mind meghalt')
        break
    
    freed = False
    number += 1
if number == 100 :
    print('tul lett elve')


