n = int(input())
nums = list(map(int, input().split()))

def part_sum(n, nums):
    dp = [0] * n
    dp[0] = nums[0]
    max_sum = dp[0]

    for i in range(1, n):

        dp[i] = max(dp[i-1] + nums[i], nums[i]) # (이전 합 + 현재 수)와 현재 수 크기 비교
        max_sum = max(max_sum, dp[i])

    return max_sum

print(part_sum(n, nums))



#점화식 : dp[i] = max(dp[i-1] + nums[i], nums[i])