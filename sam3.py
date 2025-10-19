def count_digits(s):
    count_dict = {}
    for char in s:
        num = int(char)
        count_dict[num] = count_dict.get(num, 0) + 1
    sorted_items = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    top_three = dict(sorted_items[:3])
    return top_three

result = count_digits("123456789012345")
print(result)