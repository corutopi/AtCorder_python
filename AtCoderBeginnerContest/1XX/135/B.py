

def solve():
    N = int(input())
    p = [int(i) for i in input().split()]
    p_sort = sorted(p)
    count = 0
    for i in range(N):
        if p[i] != p_sort[i]:
            count += 1
        if count >= 3:
            break
    if count in [0, 2]:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    solve()
