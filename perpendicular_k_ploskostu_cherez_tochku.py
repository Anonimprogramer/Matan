x=[]
y=[]
z=[]
i=0
for i in range(2):
    p=0
    x1=0
    y1=0
    z1 = 0
    q = 1
    s = input()
    for j in s:
        if j=='-':
            q=-1
        elif j==' ':
            p=p+1
            q=1
        elif p==0:
            x1=x1*10+float(j)*q
        elif p==1:
            y1=y1*10+float(j)*q
        elif p==2:
            z1=z1*10+float(j)*q
    x.append(x1)
    y.append(y1)
    z.append(z1)
print('(x-',x[0],')/',x[1],'=','(y-',y[0],')/',y[1],'=','(z-',z[0],')/',z[1])