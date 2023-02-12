"""
A - Favorite Sound
"""


def solve():
    A, B, C = map(int, input().split())
    ans = B // A
    if ans > C:
        ans = C
    print(ans)


if __name__ == '__main__':
    solve()
