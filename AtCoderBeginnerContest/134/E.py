

def solve():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    color_list = [-1]
    min_A = min(color_list)
    for a in A:
        if min_A < a:
            for i in range(len(color_list)):
                tag = color_list[i]
                if tag < a:
                    color_list[i] = a
                    if tag == min_A:
                        min_A = min(color_list)
                    break
        else:
            color_list.append(a)
            min_A = a
    # print(color_list)
    print(len(color_list))


if __name__ == '__main__':
    solve()
