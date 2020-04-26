def solve():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(input())

    A.sort()
    count = 1
    if N != 1:
        for i in range(1, N):
            if A[i - 1] != A[i]:
                count += 1
    print(count)


if __name__ == '__main__':
    solve()
