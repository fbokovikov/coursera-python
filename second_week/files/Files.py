f = open('filename', 'w')

f.write('Text')

f.close()

f = open('filename', 'r+')
f.read()

f.tell()
f.seek(0)
f.tell()
f.readline()
f.readlines()

#контекстный мененджер закроет файл за тебя
with open('filename') as f:
    print(f.read())
