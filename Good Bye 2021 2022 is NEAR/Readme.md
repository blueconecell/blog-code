[Good Bye 2021: 2022 is NEAR - A. Integer Diversity](https://codeforces.com/contest/1616/problem/A)

[문제설명]
 N개의 정수가 주어진다.  정수에 음수를 부여할 수 있다. **이 정수 배열에서 각기다른 숫자의 값의 최대값을 구하여라.**

 예를 들어, **[1 2 1 2 2]** 인 정수 배열은 각기다른 숫자의 값이 2개이다. 1 2가 2개이상 중복되므로 하나씩 음수로 변환시키면 **[1 -1 2 -2 2]** 로 볼 수 있다. 이 배열은 각기다른 숫자의 값이 4개이다.(원소의 수는 5개이지만 2가 2개이므로 겹친다)

 **[1 1 -1 2 2 -2]**인 정수 배열은 중복되는 값을 음수로 변환시켜도 어짜피 겹침으로 이 배열도 마찬가지로 각기다른 숫자의 값이 4개이다.
 
```
# 테스트 케이스 개수
t = int(input())
for p in range(t):
	
    #테스트 케이스에 사용되는 원소의 수 
    n=int(input())

	#출력할 결과 값
    ans=0
    
    #정수배열 입력
    s = list(map(int,input().split()))
    
    #정수배열 중복값 확인에 사용되는 딕셔너리
    count={}

    for i in s:
    	#중복되는 값이 있으면 +1
        try: count[abs(i)] += 1
        #중복되는 값이 없고 처음 나오는 값이면 value=1로 새로 만들어준다
        except: count[abs(i)] = 1
    
    #중복값 확인용 딕셔너리를 통해 결과값을 구한다
    for j in count:
    	 #value==0 일때
        if j==0:
            ans +=1
        
        #value==1 일때
        elif count.get(j)==1:
            ans+=1
         #value >=2 일때
        else:
            ans+=2
    print(ans)
    ```
정수배열 중복값을 확인할 때 1, -1은 따로 계산하지 않고, 절대값을 씌워서 같이 계산하였다.

(https://codeforces.com/contest/1616/problem/A)
