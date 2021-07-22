import collections
def findTheDifference_issac(s: str, t: str) -> str:
    s_counter = collections.Counter(s)
    t_counter = collections.Counter(t)
    for key in t_counter:
        if key not in s_counter:
            return key
        else:
            if t_counter[key] != s_counter[key]:
                return key

print(findTheDifference_issac("a", "aa"))



