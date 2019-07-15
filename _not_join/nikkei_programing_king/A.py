"""
A - Subscribers
"""


def solve():
    N, A, B = map(int, input().split())
    max_both = B if A > B else A
    min_both = (A + B) - N if (A + B) > N else 0
    print(max_both, min_both)


if __name__ == '__main__':
    solve()
