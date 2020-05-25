# read sample.txt and print the number of lines
file = open('sample.txt', 'r')
no_lines = 0
for _ in file:
    no_lines += 1
print(no_lines)
file.close()
