import random

array = random.sample(range(0,10), 10) #0~9랜덤

print(array)

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)) :
        if array[min_index] > array[j] :
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)