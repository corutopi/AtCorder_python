def solve():
    N, M = map(int, input().split())
    A = []
    if M != 0:
        A = [int(input()) for _ in range(M)]
    A.sort(reverse=True)
    mm = 10 ** 9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1  # 0段目に行くパターンは1とする
    tag = -1
    if len(A) != 0:
        tag = A.pop()
    # 1段目のパターンを設定
    if tag == 1:
        dp[1] = 0
        if len(A) == 0:
            tag = -1
        else:
            tag = A.pop()
    else:
        dp[1] = 1
    for i in range(2, N + 1):
        if i == tag:
            if len(A) == 0:
                tag = -1
            else:
                tag = A.pop()
            continue
        dp[i] = (dp[i - 1] + dp[i - 2]) % mm
    print(dp[N])


if __name__ == '__main__':
    solve()
