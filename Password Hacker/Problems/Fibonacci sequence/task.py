def fibonacci(n):
    if n == 1:
        yield [0]
    elif n == 2:
        yield 0
        yield 1
    else:
        yield 0
        yield 1
        x = 0
        y = 1
        for _ in list(range(2, n)):
            z = x + y
            yield z
            x = y
            y = z
