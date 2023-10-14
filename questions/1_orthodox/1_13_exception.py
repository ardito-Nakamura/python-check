# 次の実行結果を得られるように{A}, {B}を書き換えてください。

# [ 実行結果 ]
# huruikeya
# kawazutobikomu
# mizuno-oto
# Basho

class AnException1(Exception):
    pass


class AnException2(Exception):
    pass


def raise_frog_exception(a):
    print(a)
    print('kawazutobikomu')
    # {A}
    print('a-omoshiroi')


def func(key_: int):
    try:
        if key_ == 0:
            raise_frog_exception('huruikeya')
    except AnException1:
        print('mizuno-oto')
        # {B}
    else:
        print('mushinokoe')


try:
    func(0)
except AnException2:
    print("Wasao")
except Exception:
    print('Basho')
