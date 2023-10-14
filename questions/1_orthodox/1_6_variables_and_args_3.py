i = 5
i = 6


def f(arg=i):
    i = 7
    i += arg
    print(arg)


i = 8
i = 9

f()
