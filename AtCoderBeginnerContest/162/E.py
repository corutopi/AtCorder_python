
def solve(N, K):
    mod = 10 ** 9 + 7
    multiples = [[] for _ in range(K + 1)]
    for k in range(1, K + 1):
        for i in range(k, K + 1, k):
            multiples[k].append(i)

    gcdcounts = [0] * (K + 1)  # gcd 毎の組み合わせ個数
    gcdsums = [0] * (K + 1)   # gcd 毎の合計値
    for k in reversed(range(1, K + 1)):
        x = pow(len(multiples[k]), N, mod)
        for l in multiples[k]:
            x -= gcdcounts[l]
        gcdcounts[k] = x % mod
        gcdsums[k] = x * k % mod
    print(sum(gcdsums) % mod)


if __name__ == '__main__':
    N, K = map(int, input().split())
    solve(N, K)
