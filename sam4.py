sentence = input("Введите предложение на английском: ")

print("Длина предложения:", len(sentence))

print("В нижнем регистре:", sentence.lower())

vowels = ['a', 'e', 'i', 'o', 'u']
count=0
for char in sentence.lower():
    if char in vowels:
        count+=1

print("После замены:", sentence.replace("ugly", "beauty"))

if sentence.startswith("The"):
    print("Начинается с 'The':", sentence.startswith("The"))
if sentence.endswith("end"):
    print("Заканчивается на 'end':", sentence.endswith("end"))