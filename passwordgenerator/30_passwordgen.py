from fileinput import close
import string
import random
s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4=string.punctuation

passlen=int(input("Enter password length:\n"))
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
random.shuffle(s)
f=open("password.txt",'w')
f.write("".join(s[0:passlen]))
f.close()
print("".join(s[0:passlen]))