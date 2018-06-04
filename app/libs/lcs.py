def LCS(a, b):
    c = [0] * len(b)
    al = []
    for i in range(len(a)):
        tmp = a[i]
        for j in range(len(b)):
            js = len(b) - 1 - j
            if tmp == b[js]:
                if js == 0:
                    c[js] = 1
                else:
                    c[js] = c[js - 1] + 1
            else:
                if js != 0 and c[js - 1] != 0:
                    al.append(c[js - 1])
                c[js] = 0
    for i in range(len(b)):
        if c[i] != 0:
            al.append(c[i])
    return al