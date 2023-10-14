l = []
for i in range(1, 10):
    """3の倍数でバカになるfor文"""
    if i % 3 == 0:
        l.append(f"{i}!!!")
        # break # 出力は？
    else:
        l.append(str(i))

else:
    l.append("thanks.")

print(", ".join(l))
# 出力は？
