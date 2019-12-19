f=open("test.txt","r")
f1=open("text1a.txt","w")
k=1
for lines in f:
	f1.write(str(k) +' '+ lines)
	k=k+1

f.close()
f1.close()    