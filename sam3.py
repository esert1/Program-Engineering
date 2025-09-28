x = int(input())
if x < 0 or x > 10: 
    print("Неверный диапазон") 
    exit()
if x <= 3: 
    print("от 0 до 3 включительно")
elif x <= 6: 
    print("от 3 до 6")
else: 
    print("от 6 до 10 включительно")