import math

def solve():
    N, K = map(int, input().split())
    result = 0
    for i in range(1, N + 1):
        cn = 0
        if i >= K:
            cn = (1 / N)
        else:
            cn = (1 / N) * ((1 / 2) ** math.ceil(math.log2(K / i)))
        # print(i, '得点の時:', cn)
        result += cn
    print(result)


if __name__ == '__main__':
    solve()
