import random

final_state = [1,2,3,4,5,6,7,8]
initial_state = [2,3,4,1,6,5,8,7]

#Depth-First Search for sort list
#random swap number in list with no condition 

count = 0
num = 0
while count == 0:
    num += 1
    print(f'Round: {num}')
    print(f'Before swap: {initial_state}')
    index1 = random.randint(0,len(final_state)-1)
    index2 = index1 - 1
    keep1 = initial_state[index1]
    keep2 = initial_state[index2]
    #swap keep1 and keep2 by insert method
    initial_state[index2] = keep1
    initial_state[index1] = keep2
    #print Depth-First Search Operation
    print(f'First number is {keep1}')
    print(f'Second number is {keep2}')
    print(f'After swap: {initial_state}')
    print('---------------------------------')
    if initial_state == final_state:
        count = 'finish'
        print(f'Done in {num} times')




