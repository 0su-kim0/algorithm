

첫 줄에 테스트케이스의 수, 각 테스트케이스는 두 줄로 이루어져 있다.

테스트케이스의 첫 번째 줄에는 문서의 개수 N



import heapq as h

T=int(input())

for i in range(T):
    N,M=map(int,input().split())
    Prio=map(int,input().split())

    max_h=[-num for p in Prio]
    h.heapify(max_h)
    
    result=-h.heappop(max_pop)
    
hq=[]

for i in range(T):
    

h.heappush(hq,())


rotate