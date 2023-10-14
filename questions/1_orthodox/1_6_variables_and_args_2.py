i = 5
i = 6


def f(arg=i):
    i = 7
    print(arg)


i = 8
i = 9

f()
