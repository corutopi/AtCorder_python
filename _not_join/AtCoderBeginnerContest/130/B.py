

def solve():
    N, X = map(int, input().split())
    L = [int(i) for i in input().split()]
    bound = 0
    count = 1
    for Li in L:
        bound += Li
        if bound <= X:
            count += 1
        else:
            break
    print(count)


if __name__ == '__main__':
    solve()