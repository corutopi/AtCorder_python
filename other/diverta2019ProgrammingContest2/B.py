
# from collections import Counter

def solve():
    N = int(input())
    XY = [[int(i) for i in input().split()] for _ in range(N)]
    # print(XY)
    length_list = []
    for i in range(N):
        xi, yi = XY[i]
        for j in range(N):
            if i == j:
                continue
            xj, yj = XY[j]
            length_list.append([xi - xj, yi - yj])
    # print(length_list)
    max_count = 0
    for xy in length_list:
        count = length_list.count(xy)
        max_count = max(max_count, count)
    # print(max_count)
    print(N - max_count)


if __name__ == '__main__':
    solve()
