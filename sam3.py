def text_statistics():
    with open('input_4.txt', 'r') as file:
        lines = file.readlines()
    
    letter_count = 0
    word_count = 0
    
    for line in lines:
        letter_count += sum(c.isalpha() for c in line)
        word_count += len(line.split())
    
    print(f"Input file contains:\n{letter_count} letters\n{word_count} words\n{len(lines)} lines")

text_statistics()