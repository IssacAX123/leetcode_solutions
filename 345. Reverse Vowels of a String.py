def reverseVowels_issac(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o','u']
    s_array = [letter for letter in s]
    letter_stack = []
    for i, letter in enumerate(s_array):
        if letter.lower() in vowels:
            letter_stack.append(letter)
            s_array[i] = None
    for i in range(len(s_array)):
        if s_array[i] == None:
            s_array[i] = letter_stack.pop()
    return "".join(s_array)

def reverseVowels_issac_2(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o','u']
    s_array = [letter for letter in s]
    left_pointer = 0
    right_pointer = len(s)-1
    while left_pointer < right_pointer:
        if s_array[left_pointer].lower() in vowels and s_array[right_pointer].lower() in vowels:
            tmp = s_array[left_pointer]
            s_array[left_pointer] = s_array[right_pointer]
            s_array[right_pointer] = tmp
            left_pointer += 1
            right_pointer -= 1
        if s_array[left_pointer].lower() not in vowels:
            left_pointer += 1
        if s_array[right_pointer].lower() not in vowels:
            right_pointer -= 1
    return "".join(s_array)

print(reverseVowels_issac_2("leetcode"))