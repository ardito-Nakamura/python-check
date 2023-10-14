# 以下と同じ実行結果になるよう{A}を1行で書き換えてください。

# [ 実行結果 ]
# {0: "Now", 1: "is", 2: "better", 3: "than", 4: "never"}

Zen = ["Now", "is", "better", "than", "never"]

dict_ = {i: Zen[i] for i in range(0, len(Zen))}  # {A}

print(dict_)
