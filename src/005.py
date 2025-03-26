# match these
f = open("file1", 'r')
f = open("file2", 'r', -1)
f = open(filename, 'r')

# but do not match these
f = open("file1", 'w')
f = open("file2", 'w')
