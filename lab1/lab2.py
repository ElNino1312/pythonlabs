'''
#lab2.1
print("Вы находитесь в пещере на развилке. Вы можете пойти [Налево], [Направо] или [Прямо].\n")
print("Введите одно из слов в скобках для выбора.\n")
a = input()
if a == "Налево" or a == "направо":
    print("Вы направились налево. Через некоторое время вы доходите до металической двери. Пройдя через нее, вы оказываетесь в чистом поле, а позади вас нет никикой двери")
elif a == "Прямо" or "прямо":
    print("Спустя несколько минут, вы оказываетесь перед лестнице, ведущей [вверх] и [вниз]\n")
    print("Введите одно из слов в скобках для выбора.\n")
    a = input()
    if a == "Вверх" or "вверх":
        print("Поднявшись вверх, вы оказываетесь на платформе где стоит. Зайдя и заняв свое место, поезд начинает двигаться")
    elif a =="Вних" or "вниз":
        print("Вы начинаете спускаться вниз. Но пройдя несколько пролетов, вы замечаете что уже проходили этот этаж. Пытаясь вернутся назад, вы вновь оказываетесь на нем. Это конец")
    else: print("Некорректный ввод данных")
elif a == "Право" or "право":
    print("Идя по коридору, вы оказываетесь перед подземным озером. Но вас подстерегала гигантская подземная жаба, которая проглотила вас целиком!")
else: print("Некорректный ввод данных")
'''

'''
#lab2.2
print("Введите логин и резервный адрес\n")
login = input()
mail = input()
log = True
m = False
i=0
for i in range(len(login)):
    if login[i] == "@":
        log = False
for i in range(len(mail)):
    if mail[i] == "@":
        m = True
if m and log:
    print("OK")
elif not log:
    print("Некорректный логин")
elif not m:
    print("Некорректный адрес")
'''

'''
#2.3
print("Как прошел Ваш день?")
a=input()
if "Хорошее" or "хорошее" or "прекрасно" or "Прекрасно" in a:
    print("Отлично, у меня тоже всё хорошо :)")
elif "Плохо" or "плохо" in a:
    print("Ничего, скоро всё наладится")
elif "не" or "?":
    print("Простите, я Вас не понимаю")
else:
    print("Простите, я Вас не понимаю")
'''

#2.4
a=input()
b=input()
if (a=="да" or a=="нет") and (b=="да" or b=="нет"):
    print("ВЕРНО")
else:
    print("НЕВЕРНО")
