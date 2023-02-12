

def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    count = 0
    for i in range(N):
        count += min(A[i], B[i])
        if A[i] < B[i]:
            b = B[i] - A[i]
            count += min(A[i + 1], b)
            A[i + 1] = max(0, A[i + 1] - b)
    print(count)


if __name__ == '__main__':
    solve()
