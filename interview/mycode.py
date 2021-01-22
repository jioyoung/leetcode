def calculateScore(string1, string2):
    l1= len(string1)
    l2 = len(string2)
    L = min(l1,l2)
    res = 0
    for i in range(1, L+1):
        if string1[l1-i:] == string2[:i]:
            res = i
    return res