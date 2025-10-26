import re

def filter_text():
    with open('forbidden.txt', 'r') as file:
        forbidden_words = file.read().split()
    
    text = "Hello, world! Python is the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"
    print("Исходный текст:")
    print(text)
    
    for word in forbidden_words:
        text = re.sub(rf'\b{re.escape(word)}\b', '*' * len(word), text, flags=re.IGNORECASE)
    
    print("\nОтфильтрованный текст:")
    print(text)

filter_text()