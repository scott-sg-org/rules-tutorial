fout = open("/tmp/example1.txt", 'r', buffering=1024)
print("do stuff in here")
print("more stuff")
fout.write("whoops, I'm not writable!")
