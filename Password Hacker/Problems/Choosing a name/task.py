import itertools

# first_names and middle_names are pre-defined lists
for name in itertools.product(first_names, middle_names):
    print(*name)
