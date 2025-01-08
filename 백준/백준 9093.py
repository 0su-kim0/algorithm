import sys

N=int(input())

for _ in range(N):
    words=sys.stdin.readline().split()
    for i in words:
        reversed_words=list(i)
        reversed_words.reverse()
        print("".join(reversed_words),end=' ')
    print()
        
'''    for _ in range(len(list(i))):
        list(i).reverse()
        print(list())
        print(list(i).reverse())'''
    
'''
sys.stdin.readline().rstrip().split() (O)
**진행순서
1. sys.stdin.readline()로 입력받음. 끝에 \n이 포함
2. rstrip()으로 줄바꿈 문자 제거
3. split()으로 공백 기준으로 입력된 문자열을 리스트로 나눔

sys.stdin.readline().split().rstrip() (X)
1. 입력받음
2. 공백을 기준으로 문자열을 나눈 리스트 반환
3. 리스트객체에는 rstrip이 없음

Q) sys.stdin.readline().split()에서 그럼 공백도 리스트에 들어감?
A) X, 공백 기준으로 나눈거라 안들어감

<잘못 작성한 코드>
1.
val=list(sys.stdin.readline().rstrip().split())

split()은 리스트를 반환하기때문에 list를 사용할 필요 없음
rstrip()도 공백을 기준으로 문자열을 나누기 때문에 split을 사용하면 줄바꿈 문자는 제거됨

2.
for i in len(val)

원인: int객체는 iterable하지 않다

결론:
    len(val) > range(len(val))

    or

    len(val) > val

3.
reversed_words=list(i).reverse()

원인: 리스트를 뒤집지만, 결과반환을 하지 않음. 리스트 자체를 제자리에서 수정하고, None을 반환
        reversed_words=None이 저장됨

결론:
    reversed_words = list(i)
    reversed_words.reverse()

    or

    reversed_words = list(reversed(list(i)))

+)리스트 뒤집는게 결과 반환하는거라고 생각했는데 헷갈림
차이점: 제자리(in-place)변경, 새 객체 반환

'''


'''
모범답안


T = int(input())

for _ in range(T):
    # 한 줄 입력 받고 공백을 기준으로 단어 분리
    sentence = input().split()
    
    # 각 단어를 뒤집어서 리스트로 저장
    reversed_words = [word[::-1] for word in sentence]
    
    # 뒤집힌 단어들을 공백으로 구분해서 출력
    print(" ".join(reversed_words))
    
    
t = int(input())
for i in range(t):
    a = list(map(str,input().split(" ")))
    b = []
    for s in a:
        b.append(s[::-1])
    print(*b)
'''