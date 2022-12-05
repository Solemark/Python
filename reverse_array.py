def reverse_array(a1: any) -> any:
    c = len(a1)-1
    x = 0
    y = 0
    i = 0
    while (i <= c):
        x = a1[i]
        y = a1[c]
        a1[i] = y
        a1[c] = x
        i+=1
        c-=1
    return a1
    