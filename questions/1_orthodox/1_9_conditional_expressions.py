# 次のコードの{A}を1行で記述してください。

l = []
for i in range(0, 10):
    # {A...
    if i % 2 == 0:
        i_ = f"{i}は2の倍数"
    else:
        i_ = f"{i}は2の倍数ではない"
    # }
    l.append(i_)
