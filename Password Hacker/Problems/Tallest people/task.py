def tallest_people(**kwargs):
    p = {}
    tall = 0
    for key, value in kwargs.items():
        p[key] = value
        if value > tall:
            tall = value

    pt = []
    for key, value in p.items():
        if value == tall:
            pt.append(key)

    pt.sort()
    for i in pt:
        print("{} : {}".format(i, p[i]))
