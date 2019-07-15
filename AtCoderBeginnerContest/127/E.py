from math import factorial


def solve():
    N, M, K = map(int, input().split())

    costs = []
    for n in range(1, N + 1):
        for m in range(1, M + 1):
            costs.append(abs(n - m))
    print(costs)
    count = cmb(N * M, K) - cmb(N * M - 1, K)
    print(cmb(N * M, K))
    print(cmb(N * M - 1, K))
    print(int((sum(costs) * count) % 1000000007))


def cmb(n, r):
    return factorial(n) / factorial(r) / factorial(n - r)


if __name__ == '__main__':
    solve()
