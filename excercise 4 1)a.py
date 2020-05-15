#exercise 4 progrm 10
a=[]
x=int(input("enter the index number" ))
y=int(input("enter the element "))
a.append(y)
i=len(a)-1
while(i>x):
    a[i]=a[i-1]
    i=i-1
a[i]=y
print(a)
