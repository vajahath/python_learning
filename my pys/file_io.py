# file i/o

#write
f= open('fileIO/sample_input.txt', 'w')
f.write('buhahahha\nhello')
f.close()


#read
f= open('fileIO/sample_input.txt', 'r')
print f.read()
f.close()
