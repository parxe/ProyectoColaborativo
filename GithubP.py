for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("Cola")
    elif i % 3 == 0:
        print("Buzz")
    elif i % 5 == 0:
        print("Cola")
    else:
        print(i)
