l1 = [1, 2, 3]
l2 = ["a", "b", "c"]

zip_ = zip(l1, l2)
l_zipped = {i: s for i, s in zip_}
print(l_zipped)
