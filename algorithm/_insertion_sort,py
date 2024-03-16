import random

array = random.sample(range(0,10), 10)

for i in range(1, len(array)) :
    for j in range (i, 0, -1) : # i 값부터 0까지 -1
        if array[j] < array[j - 1]:
            array[j - 1], array[j] = array[j], array[j - 1]
        else:
            break

print(array)
