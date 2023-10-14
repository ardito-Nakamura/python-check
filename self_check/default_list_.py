def culc(a, b=1, squares=[], cubes=[]):
    """
    リストや辞書などの更新可能（ミュータブル）なオブジェクトをデフォルト値として指定した場合、
    そのオブジェクトは関数定義時に生成され、該当の引数を省略して関数を呼び出すと同じオブジェクトが使われる。
    デフォルト引数は再定義されないだけで、上書きされないわけではないため、実は矛盾しない。
    """
    squares.append(a ** 2)
    cubes.append(b ** 3)
    return squares, cubes


print(culc(1))
print(culc(2, 3))
print(culc(3, 4, [], []))
print(culc(2, 3))  # 高難度、デフォルト引数はあくまで再定義されない点に注意。
