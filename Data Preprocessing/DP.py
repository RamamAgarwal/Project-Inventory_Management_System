f=open('sample.txt','r')
print(f.read())
f.close()

fd=open('sample.txt','r')
txt=fd.read()
txt.replace('\n\n',' ')
fd.close()

#Paragraphs
para= txt.split('\n\n')
print(para)
print(len(para[:-1]))

#Words
words= txt.split(' ')
print(words)
print(len(words))

#Lines
lines= txt.split('.')
print(lines)
print(len(lines))

#Formatting
for i in range(5,16):
    patt= "[" + str(i) + "]"
    txt= txt.replace(patt,"")
print(txt)

for i in "@#$%^":
    txt= txt.replace(i,"")
print(txt)