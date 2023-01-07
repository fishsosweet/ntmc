def CTT(x,L):
    dung=0
    i=0
    while ((dung==0)and(i<len(L))):
        if x<=L[i]:
            dung=1
        else:
            i=i+1
    L.insert(i,x)
L=[1,3,5,7,9,11]
print('ds : ',L)
