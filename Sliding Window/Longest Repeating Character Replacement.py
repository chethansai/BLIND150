import collections


def rep():
    s = "AABABBA"
    k = 1
    d = collections.defaultdict(int)
    m = 0
    start = 0
    a = 0
    for i in range(0, len(s)):
        d[s[i]] += 1
        m = max(m,d[s[i]])
        if (i - start + 1) - m <= k:
            a = max(a, i - start + 1)
        else:
            d[s[start]] -=1
            start += 1

    print(a)
rep()