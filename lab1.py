
"""
#лаба 1.1

print("Введите имя и фамилию")
name = input()
print("Введите ваше любимое животное")
animal = input()
print("Введите ваш знак зодиака")
zodiac = input()

print("Индивидуальный гороскоп для пользователя "+name+"\nКем вы были в прошлой жизни: "+animal+"\nВаш знак зодиака - "+zodiac+", поэтому вы - тонко чувствующая натура.")
"""

"""
#лаба 1.2
print("1 бит - минимальная единица количества информации.\n")
print("1 байт = 8 бит.\n")
print("1 Килобит = 1024 бита.\n")
print("1 Килобайт = 1024 байта.\n")
print("1 Килобайт = 8192 бит.\n")
"""

#лаба 1.3
spisok=["","",""]
i=0
while i < 3:
    print("---")

    spisok[i] = input()
    i=i+1

print("---")
j=i-1
for i in range(len(spisok)):
    print(spisok[j])
    j-=1