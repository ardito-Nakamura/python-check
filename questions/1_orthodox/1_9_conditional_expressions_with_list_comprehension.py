# 次のコードのを1行で記述してください。

l = []
for i in range(0, 10):
    # {A...
    if i % 2 == 0:
        i_ = f"{i}は2の倍数"
    else:
        i_ = f"{i}は2の倍数ではない"
    # }
    l.append(i_)

# ヒント: 以下のコードの出力は同じ
l1 = []
for i in range(0, 10):
    i = i + 1
    l1.append(i)

l2 = [i + 1 for i in range(0, 10)]
print(l1)
print(l2)
