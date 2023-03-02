import math

def exclude_power_of_two(nums):
    total = 0
    count = 0
    for num in nums:
        if math.log2(num) % 1 != 0:
            total += num
            count += 1
    return math.floor(total/count)
nums = [11, 20, 33, 44, 51, 6, 7, 40, 9, 10]
result = exclude_power_of_two(nums)
print(result)  

