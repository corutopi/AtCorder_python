import math


def solve():
    N, D = map(int, input().split())
    X = [[int(i) for i in input().split()] for _ in range(N)]
    count = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            distance = 0
            for d in range(D):
                distance += (X[i][d] - X[j][d]) ** 2
            if math.sqrt(distance) % 1 == 0:
                # print('i:', i, 'j', j)
                count += 1
    print(count)


if __name__ == '__main__':
    solve()
