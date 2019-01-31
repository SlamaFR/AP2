d = {}
lst = [1, 2, 3, 4, 5]
d['a'] = lst
d['b'] = lst
d['c'] = d['a']
d['d'] = lst * 1
lst[0] = 5
d['c'][1] = 3
d['d'][2] = 10
print(d['a'], d['b'], d['c'], d['d'])

# Ce programme affiche 4 listes, dont 3 sont identiques :
# [5, 3, 3, 4, 5] [5, 3, 3, 4, 5] [5, 3, 3, 4, 5] [1, 2, 10, 4, 5]
