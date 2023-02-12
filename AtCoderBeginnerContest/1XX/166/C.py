def solve():
    N, M = map(int, input().split())
    height = [int(i) for i in input().split()]
    neighbor = [[-1] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        neighbor[A - 1].append(height[B - 1])
        neighbor[B - 1].append(height[A - 1])

    func = lambda i: 1 if height[i] > max(neighbor[i]) else 0
    count = sum([func(i) for i in range(N)])
    print(count)


if __name__ == '__main__':
    solve()
