def inverse(a, p):
    a_, p_ = a, p
    x, y = 1, 0
    while p_:
        t = a_ // p_
        a_ -= t * p_
        a_, p_ = p_, a_
        x -= t * y
        x, y = y, x
    x %= p
    return x


def solve():
    N, M, K = map(int, input().split())
    mod = 998244353

    nCi = [1]
    for i in range(1, N):
        nCi.append(nCi[i - 1] * (N - i) * inverse(i, mod) % mod)
    ans = 0
    for k in range(K + 1):
        n = N - k
        ans += M * int(pow((M - 1), n - 1, mod)) * nCi[k]
        ans %= mod
    print(ans)


if __name__ == '__main__':
    solve()
