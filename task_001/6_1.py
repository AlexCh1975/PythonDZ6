# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25] 

from random import randint

def create_list(size: int):
    nums = [randint(1, 100) for i in range(size)]
    return nums

def transformation_list(nums: list):
    new_nums = [nums[i] for i in range(1, len(nums)) if nums[i] > nums[i-1]]
    return new_nums            


nums = create_list(int(input("Размер списка: ")))
print(nums)
print(transformation_list(nums))