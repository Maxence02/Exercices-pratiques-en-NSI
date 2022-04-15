def nb_batiments_eclaires(hauteurs):
    n = 0
    if hauteurs == [] :
        return n
    maximum = hauteurs[0]
    for i in range(len(hauteurs)):
        if i == 0 and hauteurs[0] != 0 or hauteurs[i] > maximum :
            maximum = hauteurs[i]
            n += 1
    return n


print(nb_batiments_eclaires([]))

# tests

assert 4 == nb_batiments_eclaires([2, 1, 2, 4, 0, 4, 5, 3, 5, 6])
assert 1 == nb_batiments_eclaires([0, 3, 1, 2])
