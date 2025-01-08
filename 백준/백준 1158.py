#####못품


import sys
from collections import deque

N,K=map(int,input().split())

queue=deque(range(1,N+1))
left=[]

while queue:
    
    for i in range(N*K):
        if i%3==2:
            left.append(queue.popleft())
        else:
            queue.append(queue.popleft())