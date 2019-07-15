def solve():
    H, W = map(int, input().split())
    CELL = [[False for _ in range(W + 2)]]
    grid = [[-1, -1, -1] * (W + 2)] * (H + 2)
    for _ in range(H):
        CELL.append([False] + [s == '.' for s in list(input())] + [False])
    CELL.append([[False for _ in range(W + 2)]])

    from collections import deque
    for i in range(H * W):
        que = deque([i])
        while que.count > 0:
            tag = que.pop()
            h, w = divmod(i, W)
            h += 1
            w += 1
            if grid[h][w][2] != -1:
                continue

        pass



if __name__ == '__main__':
    solve()
