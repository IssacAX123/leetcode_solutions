import collections


def palindrome_permutation_issac(s: str) -> bool:
    counter = collections.Counter(s)
    single_odd_found = False
    for key in counter:
        if counter[key] % 2 == 1 and single_odd_found:
            return False
        if counter[key] % 2 == 1 and not single_odd_found:
            single_odd_found = True
    return True

print(palindrome_permutation_issac("racecap"))