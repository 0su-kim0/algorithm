# N과 M(1)


N,M=map(int,input().split())
ans=[]

def bt():
    if len(ans)==M:
        print(" ".join(map(str,ans)))
        return   
    for i in range(1,N+1):
        if i not in ans: # i가 ans에 없다면
            ans.append(i) # 값 추가
            bt() # 다음 루프
            ans.pop() # 끝난 후 원소 없앰
bt()    

# 백트래킹(backtracking)은 
# 재귀적으로 모든 경우의 수를 탐색하면서 
# 조건에 맞는 결과만을 출력하거나 저장하는 방식