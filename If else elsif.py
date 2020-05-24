a = int(input("First number:"))
b = int(input("Second number:"))
c = int(input("Third number:"))
if a > b:
    print("Свершилось!")
elif a < b:
    print("Да ну!")
elif a == b:
    print("А если так?")
    a = a + c
    b = b - c
    if a > b:
        print("Свершилось!")
    elif a < b:
        print("Да ну!")
    elif a == b:
        print("А если так?")
