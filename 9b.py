with open("Q2_file1.txt","r") as f1,open('Q2_file2.txt','r') as f2:
    for i,j in zip(f1,f2):
        if set(i.split()) == set(j.split()):
            print(i.strip())
        else:
            print(i.split(),j.split())
            
with open("Q2_file1.txt","r") as f1,open('Q2_file2.txt','r') as f2:            
    for i,j in zip(f1,f2):
        if set(i.split()) == set(j.split()):
            print(i.strip())
        else:
            pass
            
with open("Q2_file1.txt","r") as f1,open('Q2_file2.txt','r') as f2:            
    for i,j in zip(f1,f2):
        if set(i.split())== set(j.split()):
            pass
        else:
            print(j.strip())
                        
with open("Q2_file1.txt","r") as f1,open('Q2_file2.txt','r') as f2:            
    for i,j in zip(f1,f2):
        if set(i.split())== set(j.split()):
            pass
        else:
            print(i.strip(),j.strip())

        