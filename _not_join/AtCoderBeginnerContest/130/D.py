

def solve():
    N, K = map(int, input().split())
    a = [int(i) for i in input().split()]
    worm = [0]
    for ai in a:
        worm.append(worm[-1] + ai)
    pointA = 0
    pointB = 0
    count = 0
    while True:
        if pointA == pointB == N:
            break
        # move pointA
        while True:
            if pointA == N:
                break
            pointA += 1
            if worm[pointA] - worm[pointB] >= K:
                count += N - pointA + 1
                break
        # move pointB
        while True:
            if pointB == pointA:
                break
            pointB += 1
            if worm[pointA] - worm[pointB] >= K:
                count += N - pointA + 1
            else:
                break
    print(count)


if __name__ == '__main__':
    solve()
