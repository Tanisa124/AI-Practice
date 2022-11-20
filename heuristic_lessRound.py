#this model aim to reduce number of rounds but will continue to use random method

import random
from datetime import datetime
start_time = datetime.now()

final_state = [1,2,3,4,5,6,7,8]
initial_state = [0,0,0,0,0,0,0,0]

#random initail state with different position of number
while 0 in initial_state:
    rand = random.randint(1,8)
    index = random.randint(0,7)
    if rand not in initial_state and rand - 1 != index:
        initial_state[index] = rand



#heuristic Search for sort list
#random swap number with heuristic condition

count = 0
num = 0
heuristic = dict()
swap = []
while count == 0:
    num += 1
    print(f'Round: {num}')
    print(f'Before swap: {initial_state}')
    #define heuristic by if number is correct position give it 1 point if not give it -1 point
    for i in range(len(initial_state)):
        if initial_state[i] == final_state[i]:
            heuristic[i] = 1
        else:
            heuristic[i] = -1
            #incorrect position number will be swap to make it correct
            swap.append(initial_state[i])
    
    less = False
    while less == False:
        #random 2 number from swap list 
        swap_items = random.choices(swap, k = 2)
        index1 = initial_state.index(swap_items[0])
        index2 = initial_state.index(swap_items[1])
        if index2 > index1 and swap_items[0] > swap_items[1]:
            initial_state[index1] = swap_items[1]
            initial_state[index2] = swap_items[0]
            less = True

    #print heuristic Search Operation
    print(f'Heuristic is {heuristic}')
    print(f'-1 point is number: {swap}')
    print(f'First number is {swap_items[0]}')
    print(f'Second number is {swap_items[1]}')
    print(f'After swap: {initial_state}')
    print('---------------------------------')
    #clear swap list to make it can append again
    swap = []
    if initial_state == final_state:
        count = 'finish'
        print(f'Done in {num} times')
        end_time = datetime.now()
        time = end_time - start_time
        print(f'Duration: {time}')




