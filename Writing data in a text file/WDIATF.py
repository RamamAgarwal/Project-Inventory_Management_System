fp=open("sample2.txt",'w')
fp.write("Hello all , Wassup?")
fp.close()
fk=open("sample1.txt",'a')
fk.write("I am in trouble!!")
fk.close()
fm=open("sample3.txt",'a')
txt=input("Enter the text: ")
txt=txt+'.\n'
fm.write(txt)
fm.close()