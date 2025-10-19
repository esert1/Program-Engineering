def slice_between_occurrences(tup, element):
    if element not in tup:
        return ()
    indices = [i for i, x in enumerate(tup) if x == element]
    if len(indices) < 2:
        return tup[indices[0]:]
    return tup[indices[0]:indices[1] + 1]

print(slice_between_occurrences((1, 2, 3), 8))
print(slice_between_occurrences((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(slice_between_occurrences((1, 2, 8, 5, 1, 2, 9), 8))