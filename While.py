def loop_func():
    a = 1
    b = 40
    c = 5
    while b > a:
        print("a = " + str(a) + " " + "Not yet.")
        a = a + c
    return str("Finally! a = ") + str(a)


print(loop_func())
