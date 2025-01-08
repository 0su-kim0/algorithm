import sys

N=int(sys.stdin.readline().rstrip())

result=[]

def finding(result):
    temp=[]
    for i in range(len(result)):
        if result[i]==')':
            if not temp:
                print('NO')
                return
            else:
                temp.pop()   
        else:
            temp.append(result[i])
    if not temp:
        print('YES')
    else:
        print('NO')

for _ in range(N):
    result=list(sys.stdin.readline().rstrip())
    finding(result)



'''


'''
    
    
    
'''
temp[]를 전역으로 잘못 선언
return과 break차이
'''