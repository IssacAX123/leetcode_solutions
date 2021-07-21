
# ewach element is an index of the array. the elements that are not negative is because they have not been accessed 
def findDisappearedNumbers_online(nums):
    for n in nums:
        i = abs(n) - 1
        nums[i] = -abs(nums[i])
    return [i + 1 for i, v in enumerate(nums) if v > 0]


print(findDisappearedNumbers_online([4, 3, 2, 7, 8, 2, 3, 1]))

