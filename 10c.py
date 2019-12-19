import io
try:
    f=open("text4.txt",'r')
    s1 = input("Enter the String:")
    f.write(s1)
#except io.UnsupportedOperation as e:
    #print(e)
except Exception as e:
    print(e)
finally:
    print("Done") 