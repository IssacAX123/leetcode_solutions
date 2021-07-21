def anagram_mapping_issac(a, b):
    map_dict = {}
    for element in a:
        map_dict[element] = -1
    for i in range(len(b)):
        map_dict[b[i]] = i

    solution_array = []
    for element in a:
        solution_array.append(map_dict[element])

    return solution_array

