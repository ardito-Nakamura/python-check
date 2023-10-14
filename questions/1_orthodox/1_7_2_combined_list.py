numbers = [1, 2, 3]
strings = ['A', 'B', 'C']

# ↓ 1行で書き換えてください。
l = []
for n in numbers:
    l.append((n, strings[numbers.index(n)]))


print(l)
