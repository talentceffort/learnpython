in_file = open('chicken.txt', 'r')

# for line in in_file:
#     print(line)

for line in in_file:
    print(line.strip())


in_file.close()
