import collections
#my one is faster
def findTheDifference_issac(s: str, t: str) -> str:
    s_counter = collections.Counter(s)
    t_counter = collections.Counter(t)
    for key in t_counter:
        if key not in s_counter:
            return key
        else:
            if t_counter[key] != s_counter[key]:
                return key

def findTheDifference_online(s: str, t:str) -> str:
    i = 0
    sum = 0
    while i < len(s):
        sum += (ord(t[i]) - ord(s[i]))
        i+= 1
    sum += ord(t[i])
    return chr(sum)

# optimal between space and time
def findTheDifference_online_2(s: str, t:str) -> str:
    i = 0
    res = 0
    while i < len(s):
        res = res ^ ord(s[i])
        res = res ^ ord(t[i])
        i+=1
    res = res ^ ord(t[i])
    return chr(res)
print(findTheDifference_online_2("aaabb", "aaabbc"))



