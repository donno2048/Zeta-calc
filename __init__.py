def zeta(num,MAX): #MAX is accuracy and this calculates ζ(num)
    factors=[0 for i in range(MAX)];P=[];C=[]
    for i in range(2,MAX):
        q=100*i/MAX
        if int(q)==q:print(f'{int(q)}%')
        if i==MAX-1:print('100%')
        if i not in C:
            P+=[i];factors[i]=1
            for j in range(i,MAX,i):C+=[j]
        else:
            for p in P:
                k=i
                for j in range(MAX):
                    k/=p
                    if int(k)!=k:break
                factors[i]=max(j,factors[i])
                if p>=MAX**2:break
    return MAX/(sum([factors.count(i) for i in range(num)]))
print(zeta(3,100))#to print out ζ(3) with low accuracy
