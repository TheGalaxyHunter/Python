# read sums.txt
file = open('sums.txt', 'r')
for line in file:
    a, b = line.split(' ')
    print(int(a) + int(b))
file.close()
