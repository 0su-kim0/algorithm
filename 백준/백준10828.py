import sys

N= int(sys.stdin.readline().rstrip())

li=[]
result=[]
for _ in range(N):
    val=list(sys.stdin.readline().rstrip().split())
    li.append(val)


def calc(N):
    for i in range(N):
        if li[i][0]=='push':
            result.append(li[i][1])
        elif li[i][0]=='pop':
            if not result:
                print(-1)
            else:
                print(result.pop())            
        elif li[i][0]=='size':
            print(len(result))
        elif li[i][0]=='empty':
            if result:
                print(0)
            else:
                print(1)
        elif li[i][0]=='top':
            if not result:
                print(-1)
            else:
                print(result[-1])
calc(N)     

'''
파이썬 스택
기본 리스트에서 append(),pop()


빈 리스트 확인 시 if result==[]: 이거보다는 
if not result: 이렇게 표현
빈 리스트는 False임
'''