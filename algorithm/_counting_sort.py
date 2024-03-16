import random

array = random.choices(range(0,10), k=15) # 중복 있는 리스트

count = [0] * (max(array) + 1)

for i in range(len(array)) :
    count[array[i]] += 1

for i in range(len(count)) :
    for j in range(count[i]) :
        print(i, end=" ")

