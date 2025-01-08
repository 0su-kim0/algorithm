N,M= map(int,input().split())
ans= []

def bt(start):
    if len(ans)==M:
        print(" ".join(map(str,ans)))
        return
    for i in range(start,N+1):
        ans.append(i)
        bt(i)
        ans.pop()
        
bt(1)