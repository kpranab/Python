file = open("input.txt", 'w')
file.write("Please write this text")
file.close()

file = open("input.txt", 'r')
content = file.read()
print(content)
# file.close()

file = open("input.txt", 'a')
file.write("\nnew line -- write this text")
file.close()