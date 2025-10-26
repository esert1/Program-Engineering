import re
from collections import Counter

def analyze_article():
    with open('article.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = len(words)
    most_common_word, frequency = Counter(words).most_common(1)[0]
    
    print(f"Общее количество слов: {word_count}")
    print(f"Самое частое слово: '{most_common_word}' (встречается {frequency} раз)")

analyze_article()