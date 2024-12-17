a = [int(s) for s in input().split()]
a[a.index(min(a))], a[a.index(max(a))] = a[a.index(max(a))], a[a.index(min(a))]
print(' '.join([str(s) for s in a]))