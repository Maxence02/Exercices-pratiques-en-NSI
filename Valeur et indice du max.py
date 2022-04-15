def valeur_et_indice_du_max(valeurs):
    m = 0
    if valeurs == [] :
        return (None, None)
    n = valeurs[0]
    for i in range(len(valeurs)) :
        if valeurs[i] > n :
            n = valeurs[i]
            m = i
    return n, m
            

# tests
assert valeur_et_indice_du_max([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3)
assert valeur_et_indice_du_max([1, 1, 1, 99, 99]) == (99, 3)
assert valeur_et_indice_du_max([10]) == (10, 0)
assert valeur_et_indice_du_max([]) == (None, None)
