# 次のコードの実行結果として正しいものはどれか。

l = [-2, 1, 0, 15, 30]
l.insert(2, 5)
l.append(45)
l.sort()
l.pop(-2)
l.sort(reverse=True)
print(l)


# [15, 5, 1, 0, -2, 45]

# [-2, 0, 1, 5, 15, 45]

# [45, 30, 15, 5, 1, 0]

# [45, 15, 5, 1, 0, -2]

# [45, 15, 5, 5, 2, 1, 0, -2]
