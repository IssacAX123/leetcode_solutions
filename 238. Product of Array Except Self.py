from typing import List


def productExceptSelf_issac(nums: List[int]) -> List[int]:
    previous_product = 1
    previous_products = []
    for num in nums:
        previous_products.append(previous_product)
        previous_product = previous_product * num

    after_product = 1
    after_products = []
    for num in nums[::-1]:
        after_products.append(after_product)
        after_product = after_product * num
    print(previous_products)
    print(after_products)
    return [a * b for a, b in zip(previous_products, after_products[::-1])]

def productExceptSelf_online(nums):
    p = 1
    n = len(nums)
    output = []
    for i in range(0, n):
        output.append(p)
        p = p * nums[i]
    p = 1
    for i in range(n - 1, -1, -1):
        output[i] = output[i] * p
        p = p * nums[i]

print(productExceptSelf_issac([1, 2, 3, 4]))
