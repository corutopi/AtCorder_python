def solve():
    N, K = map(int, input().split())
    cs = [0] * (N + 1)
    for i in range(1, N + 1):
        cs[i] = cs[i - 1] + i
    # print(cs)
    ans = 0
    for i in range(K, N + 2):
        if i == N + 1:
            ans += 1
        else:
            mn = cs[i - 1]
            mx = cs[-1] - cs[-1 - i]
            ans += mx - mn + 1
        # print(i, mx, mn, ans)
        ans = ans % (10**9 + 7)
    print(ans)


if __name__ == '__main__':
    solve()
