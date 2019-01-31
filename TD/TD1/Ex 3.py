d1 = {'a': 0, 'b': 1}
d2 = d1
d2['a'] += 1
print(d1, d2)

# Ce programme affiche deux dictionnaires identiques :
# {'a': 1, 'b': 1} {'a': 1, 'b': 1}

# Pour affecter une copie de d1 à d2, on utilise la méthode copy() :

d1 = {'a': 0, 'b': 1}
d2 = d1.copy()
d2['a'] += 1
print(d1, d2)

# Résultat :
# {'a': 0, 'b': 1} {'a': 1, 'b': 1}
