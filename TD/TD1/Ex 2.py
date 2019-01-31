d = {}
d['123'] = 1
d[[1, 2, 3]] = 2    # Il est impossible d'utiliser un objet mutable comme clé.
d[(12, 3)] = 3
d[123] = 4
print(d['0123'])    # Cette clé n'existe pas.
