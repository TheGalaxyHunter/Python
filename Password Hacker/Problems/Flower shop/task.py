import itertools

# flower_names is pre-defined lists
for i in range(1, 4):
    for comb in itertools.combinations(flower_names, i):
        print(comb)
