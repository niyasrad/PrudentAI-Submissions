from itertools import combinations

def sumEqual(a: list, b: list):
    c = []
    c_sum = []
    d = []
    d_sum = []
    for r in range(1, len(a) + 1):
        c1 = [list(x) for x in list(combinations(a, r))]
        c2 = [sum(list(x)) for x in list(combinations(a, r))]
        c.append(c1)
        c_sum.append(c2)
    c = [j for i in c for j in i]

    c_sum =  sum(c_sum, [])
    for r in range(1, len(b) + 1):
        c1 = [list(x) for x in list(combinations(b, r))]
        c2 = [sum(list(x)) for x in list(combinations(b, r))]
        d.append(c1)
        d_sum.append(c2)
    d = [j for i in d for j in i]
    d_sum =  sum(d_sum, [])
    for i in range(len(d_sum)):
        if (d_sum[i] in c_sum):
            return ("{}, {}".format(c[c_sum.index(d_sum[i])], d[i]))
    return 0

print(sumEqual([1,2,3,4,5,6], [9,10,11,12,13,14])) #[3,6], [9] Getting a different output from testcase because of combination order.
print(sumEqual([10,11,12,13,14], [2, 3, 19, 99, 101])) #[10, 11], [2, 19]