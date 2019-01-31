def init(d):
    for x in d:
        d[x] = 0


d = {'a': 'bbb', 'b': 15, (12, 4): []}
init(d)
print(d)

# Toutes les valeurs de d sont remplacées par 0 :
# {'a': 0, 'b': 0, (12, 4): 0}
