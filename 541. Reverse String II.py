def reverseStr_issac(s: str, k: int) -> str:
    s_array = [c for c in s]
    for i in range(0, len(s), 2*k):
        start = i
        end = min(i + k - 1, len(s)-1)
        while start < end:
            tmp = s_array[start]
            s_array[start] = s_array[end]
            s_array[end] = tmp
            start += 1
            end -= 1
    return "".join(s_array)

# can also us es_array[i:min(i + k, len(s))] = s_array[i:min(i + k, len(s))][::-1] for sublist reversal
print(reverseStr_issac("abcd", 4))