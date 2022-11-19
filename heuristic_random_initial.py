import random

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
    
    #random index of swap number
    rand1 = random.randint(0,len(swap)-1)
    rand2 = rand1 - 1
    #find that number in initial_state list
    index1 = initial_state.index(swap[rand1])
    index2 = initial_state.index(swap[rand2])
    #swap 2 incorrect position number
    initial_state[index2] = swap[rand1]
    initial_state[index1] = swap[rand2]
    #print heuristic Search Operation
    print(f'Heuristic is {heuristic}')
    print(f'-1 point is number: {swap}')
    print(f'First number is {rand1}')
    print(f'Second number is {rand2}')
    print(f'After swap: {initial_state}')
    print('---------------------------------')
    #clear swap list to make it can append again
    swap = []
    if initial_state == final_state:
        count = 'finish'
        print(f'Done in {num} times')




