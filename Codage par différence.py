def delta_encoding(valeurs):
    liste = []
    n = 0
    for i in range(1, len(valeurs)) :
        n = valeurs[i] - valeurs[i - 1]
        liste.append(n)
    return (valeurs[0], liste)


# tests

assert delta_encoding(
    [1_000_000, 1_000_042, 1_000_040, 1_000_055, 1_000_010]
) ==  (1000000, [42, -2, 15, -45])

assert delta_encoding([42]) == (42, [])
