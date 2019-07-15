"""
Traveling
"""


def solve():
    N = int(input())
    bt = 0
    bx = 0
    by = 0
    for _ in range(N):
        t, x, y = map(int, input().split())
        dt = t - bt
        dd = abs(x - bx) + abs(y - by)
        if dt < dd or (dt >= dd and (dd - dt) % 2 == 1):
            # print(dt, dd)
            print('No')
            return
        bt = t
        bx = x
        by = y
    print('Yes')


if __name__ == '__main__':
    solve()
