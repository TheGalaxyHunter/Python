# read test.txt
file = open('test.txt', 'r')
for line in file:
    char = line.split()[0][0]
    print(char)
file.close()
