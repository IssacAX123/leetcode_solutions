#faster
def addStrings_issac(num1: str, num2: str) -> str:
    if len(num1) > len(num2):
        min_num = num2
        max_num = num1
    else:
        min_num = num1
        max_num = num2
    result = ""
    carry = 0
    for i in range(-1, -1*len(min_num)-1, -1):
       ascii = (ord(max_num[i]) - 48) + (ord(min_num[i])-48)
       ascii += carry
       if ascii > 9:
           carry = 1
           ascii2 = ascii - 10
           result += str(ascii2)
       else:
           carry = 0
           result += str(ascii)

    for i in range(len(max_num) - len(min_num) - 1, -1, -1):
       ascii = (ord(max_num[i]) - 48) + carry
       if ascii > 9:
           carry = 1
           ascii2 = ascii - 10
           result += str(ascii2)
       else:
           carry = 0
           result += str(ascii)
    if carry == 1:
        result += "1"

    return result[::-1]

#space
def addStrings_online(num1: str, num2: str) -> str:
    result = ""
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0
    while i >= 0 or j >= 0:
        digit_sum = carry
        if i >= 0:
            digit_sum += ord(num1[i]) - ord("0")
            i -= 1

        if j >= 0:
            digit_sum += ord(num2[j]) - ord("0")
            j -= 1

        result += str(digit_sum % 10)
        carry = digit_sum // 10

    if carry == 1:
        result += "1"

    return result[::-1]


