import random


def list_creation():
    x = int(input("Enter size of the list: "))
    y = int(input("Enter a max value of the list's element: "))
    if y > 0:
        return [random.randint(0, y) for i in range(x)]
    else:
        return [random.randint(y, 0) for i in range(x)]


print(list_creation())





