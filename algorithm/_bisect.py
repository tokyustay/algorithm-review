from bisect import bisect_left, bisect_right
import random

array = random.choices(range(0, 6), k=10)

array.sort()

print(array)

def count_by_range(array, left_value, right_value) :
    left_index = bisect_left(array, left_value)
    print(left_index)
    right_index = bisect_right(array, right_value)
    print(right_index)
    return right_index - left_index

length = count_by_range(array, 4, 4)

print(length)