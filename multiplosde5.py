for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        prints("CocaCola")
    elif i % 3 == 0:
        prints("Buzz")
    elif i % 5 == 0:
        prints("Cola")
    else:
        prints(i)
