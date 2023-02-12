"""
解説を参考に作成
"""


def solve():
    N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    for _ in range(M):
        B, C = map(int, input().split())
        A += [C] * B
    A.sort(reverse=True)
    print(sum(A[:N]))


if __name__ == '__main__':
    solve()
