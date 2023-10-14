def culc(a, b=1, squares=[], cubes=[]):
    squares.append(a ** 2)
    cubes.append(b ** 3)
    return squares, cubes


# 出力は？
print(culc(1))
print(culc(2, 3))
print(culc(3, 4, [], []))
print(culc(2, 3))  # 高難度、デフォルト引数は再定義されない点に注意。
