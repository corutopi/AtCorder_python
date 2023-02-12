"""
B - K-th Common Divisor
"""


def solve():
    A, B, K = map(int, input().split())
    count = 0
    for i in reversed(range(1, A + 1)):
        if A % i == 0 and B % i == 0:
            count += 1
            if count == K:
                ans = i
                break
    print(ans)


if __name__ == '__main__':
    solve()
