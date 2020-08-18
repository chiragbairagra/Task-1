n=int(input("HOW MANY TERMA TO DISPLAY"))
n1,n2=0,1
count=0
while count<n:
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count+=1
