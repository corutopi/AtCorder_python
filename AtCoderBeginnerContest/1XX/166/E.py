def solve():
    N = int(input())
    As = [int(i) for i in input().split()]

    N_minus_A = [0] * N
    N_plus_A = [0] * N

    for i in range(N):
        minus = i + 1 - As[i]
        plus = i + 1 + As[i]
        if 0 < minus < N:
            N_minus_A[minus] += 1
        if 0 < plus < N:
            N_plus_A[plus] += 1
    print(sum([N_minus_A[i] * N_plus_A[i] for i in range(N)]))


if __name__ == '__main__':
    solve()
