# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, Si):
    Si = ['#' * (W + 2)] + ['#' + S + '#' for S in Si] + ['#' * (W + 2)]
    lamp_map = [[[-1, -1] for _ in range(W + 2)] for _ in range(H + 2)]
    ans = 0
    for h in range(1, H + 2):
        for w in range(1, W + 2):
            # block
            if Si[h][w] == '#':
                lamp_map[h][w][0] = 0
                lamp_map[h][w][1] = 0
                continue
            # vertical
            if lamp_map[h - 1][w][0] > 0:
                lamp_map[h][w][0] = lamp_map[h - 1][w][0]
            else:
                tmp = 0
                while Si[h + tmp][w] == '.':
                    tmp += 1
                lamp_map[h][w][0] = tmp
            # horizon
            if lamp_map[h][w - 1][1] > 0:
                lamp_map[h][w][1] = lamp_map[h][w - 1][1]
            else:
                tmp = 0
                while Si[h][w + tmp] == '.':
                    tmp += 1
                lamp_map[h][w][1] = tmp
            ans = max(ans, sum(lamp_map[h][w]) - 1)
    print(ans)


if __name__ == '__main__':
    H, W = map(int, input().split())
    Si = [input() for _ in range(H)]

    # # test
    # import func
    # H, W = 2000, 2000
    # Si = [''.join([func.random_str(W, '.')]) for _ in range(H)]
    # for s in Si:
    #     print(s)
    solve(H, W, Si)
