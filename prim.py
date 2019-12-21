arr = [39877,31319,39869]
for i in range(3):
    b=[1]
    for j in range(2,arr[i]):
        if(arr[i]%j!=0):
            b.append(j)
    print(b)     
