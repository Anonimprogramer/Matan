x=[]
y=[]
z=[]
i=0
q=1
xopred=0
yopred=0
zopred=0
c=[[0 for k in range(3)]for r in range(3)]
for i in range(3):
    p=0
    x1=0
    y1=0
    z1=0
    q=1
    s=input()
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
c[0][0]=-x[0]
c[0][1]=-y[0]
c[0][2]=-z[0]
c[1][0]=x[0]-x[1]
c[1][1]=y[0]-y[1]
c[1][2]=z[0]-z[1]
c[2][0]=x[1]-x[2]
c[2][1]=y[1]-y[2]
c[2][2]=z[1]-z[2]
xopred=c[1][1]*c[2][2]-c[2][1]*c[1][2]
yopred=c[1][2]*c[2][0]-c[1][0]*c[2][2]
zopred=c[1][0]*c[2][1]-c[1][1]*c[2][0]
print(xopred*c[0][0]+yopred*c[0][1]+zopred*c[0][2],'+','x',xopred,'+y',yopred,'+z',zopred)
print('конец')