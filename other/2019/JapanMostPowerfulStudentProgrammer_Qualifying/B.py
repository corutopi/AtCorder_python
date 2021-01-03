def solve():
    mod = 10 ** 9 + 7
    N, K = map(int, input().split())
    A = [int(i) for i in input().split()]
    count = 0
    for i in range(N):
        inner_count = 0
        all_count = 0
        for j in range(N):
            if A[i] < A[j]:
                all_count += 1
            if i > j and A[i] < A[j]:
                inner_count += 1
        # print('i', i, 'all', all_count, 'inner', inner_count,
        #       'A[i]', A[i],
        #       all_count * ((K - 1) * K // 2) + inner_count * K)
        count += all_count * ((K - 1) * K // 2) + inner_count * K
        count %= mod
    print(count)


if __name__ == '__main__':
    solve()
