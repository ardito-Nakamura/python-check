# 次の関数に以下のオブジェクトを使って正しく値を渡してください。

# オブジェクト:
d = {"hoge": 1, "fuga": 2, "piyo": 3}


def f_1(hoge, fuga, piyo):
    print(f"{hoge}+{fuga}+{piyo}={hoge + fuga + piyo}")


# f_1()

# 次の関数に以下のオブジェクトを使って正しく値を渡してください。

# オブジェクト:
l = [1, 2, 3]


def f_2(hoge, fuga, piyo):
    print(f"{hoge}+{fuga}+{piyo}={hoge + fuga + piyo}")


# f_2()


# 次の関数に以下のオブジェクトを使って、以下と同じ出力結果が得られるように値を渡してください。

# オブジェクト:
l_ = [1, 2, 3]
d_ = {"hoge": 1, "fuga": 2, "piyo": 3}

# 出力結果:
# ([1, 2, 3],)
# {'hoge': 1, 'fuga': 2, 'piyo': 3}


def f_3(*args, **kwargs):
    print(args)
    print(kwargs)
