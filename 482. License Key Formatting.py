#faster
def licenseKeyFormatting_issac(s: str, k: int) -> str:
    dash_count = 0
    for char in s:
        if char == "-":
            dash_count += 1
    groups = (len(s) - dash_count) // k
    remaining = (len(s) - dash_count) % k
    arrangment = [remaining] + [k for i in range(groups)] if remaining != 0 else [k for i in range(groups)]
    new_s = ""
    arrangment_pointer = 0
    arrangment_counter = 0
    for char in s:
        if char != "-":
            new_s += char.upper()
            arrangment_counter += 1
            if arrangment_counter == arrangment[arrangment_pointer]:
                arrangment_pointer += 1
                arrangment_counter = 0
                if arrangment_pointer != len(arrangment):
                    new_s += "-"
    return new_s


# really slow
def licenseKeyFormatting_online(s: str, k: int) -> str:
    s = s.upper()
    s = s.replace("-", "")
    new_string = s
    for i in range(len(s) - k-1, -1, -k):
        new_string = new_string[:i+1] + "-" + new_string[i + 1:]
    return new_string


print(licenseKeyFormatting_online("2-5g-3-J", 2))
