import random

array = random.sample(range(0,10), 10)

def quick_sort (array, start, end) :
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while(left <= right) :
        while (left <= end and array[left] <= array[start]) :
            left += 1
        while (right > start and array[right] >= array[pivot]) :
            right -= 1
        if (left > right) :
            array[pivot], array[right] = array[right], array[pivot]
        else :
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)