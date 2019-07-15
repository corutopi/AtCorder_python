"""
Common Function
"""


def combinations_count(n, r):
    import math
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def ppprint(itr_obj):
    if len(itr_obj) == 0:
        print('non list', itr_obj)
    for ite in itr_obj:
        print(ite)


def make_test_graph_data(node, edge, is_directed=False):
    import random
    count = 0
    re = []
    while count < edge:
        new = [random.randint(1, node), random.randint(1, node)]
        if new[0] == new[1]:
            continue
        if not is_directed:
            new.sort()
        if new in re:
            continue
        re.append(new)
        count += 1
    return re