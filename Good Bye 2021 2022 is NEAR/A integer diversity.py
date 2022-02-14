t = int(input())
for p in range(t):
    n=int(input())


    ans=0
    s = list(map(int,input().split()))
    count={}

    for i in s:
        try: count[abs(i)] += 1
        except: count[abs(i)] = 1
    # print(count)
    for j in count:
        if j==0:
            ans +=1
        elif count.get(j)==1:
            ans+=1
        else:
            ans+=2
    print(ans)
