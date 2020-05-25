n = int(input())


def squares(x):
    for i in list(range(x)):
        yield (i+1) ** 2


sq = squares(n)

# Don't forget to print out the first n numbers one by one here
for j in list(range(n)):
    print(next(sq))
