
N = int(input())
times = list(map(int, input().split()))


for i in range(1, len(times)):
    for j in range(i, 0, -1):
        if times[j] < times[j-1]:
            times[j], times[j-1] = times[j-1], times[j]
        else:
            break

total_time = 0
accumulated_time = 0

for time in times:
    accumulated_time += time  # 누적 시간 계산
    total_time += accumulated_time  # 총합 계산

# 출력
print(total_time)


################################
################################



N=int(input())
data=list(map(int,input().split()))

data.sort()

for i in range(N):
    *N