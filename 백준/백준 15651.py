# N과 M (3)

N,M= map(int,input().split())
ans= []

def bt():
    if len(ans)==M:
        print(" ".join(map(str,ans)))
        return
    for i in range(1,N+1):
        ans.append(i)
        bt()
        ans.pop()
        
bt()