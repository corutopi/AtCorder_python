# 解説を参考に作成


def solve(N, As, Bs):
    As.sort()
    Bs.sort()
    ans = 0
    # N が奇数の場合
    if N % 2 == 1:
        x = (N + 1) // 2 - 1
        ans = Bs[x] - As[x] + 1
    # N が偶数の場合
    else:
        lowx = N // 2 - 1
        highx = N // 2
        ans = (Bs[lowx] + Bs[highx]) - (As[lowx] + As[highx]) + 1
    print(ans)
    pass


if __name__ == '__main__':
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    solve(N, A, B)
