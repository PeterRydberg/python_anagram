filename = "eventyr.txt"
file = open(filename, "r")

words = [line.strip('\n') for line in file]

print(words)
