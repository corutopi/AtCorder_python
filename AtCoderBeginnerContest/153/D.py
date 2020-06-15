# import sys
# sys.setrecursionlimit(10 ** 6)
# from decorator import stop_watch
#
#
# @stop_watch
def solve(H):
    ans = 0
    monster = 1
    while True:
        ans += monster
        if H == 1:
            break
        H = H // 2
        monster *= 2
    print(ans)


if __name__ == '__main__':
    H = int(input())
    solve(H)
