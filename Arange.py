EPS = 10**(-6)

def arange(a, b, pas):
    liste = []
    if a == b :
        return liste
    c = a
    while c < b - EPS:
        liste.append(c)
        c = (a + pas)
        a += pas
    return liste

assert arange(2.0, 2.0, 0.1) == []

def sont_proches(x, y):
    return abs(x - y) < EPS

resultat = arange(2.0, 4.0, 0.5)
attendu = [2.0, 2.5, 3.0, 3.5]
assert len(resultat) == len(attendu), "Erreur sur la longueur renvoyée"
for x, y in zip(resultat, attendu):
    assert sont_proches(x, y), f"Erreur avec {x} qui n'est pas proche de {y} dans arange(2.0, 4.0, 0.5)"

resultat = arange(5.0, 6.5, 0.25)
attendu = [5.0, 5.25, 5.5, 5.75, 6.0, 6.25]
assert len(resultat) == len(attendu), "Erreur sur la longueur renvoyée"
for x, y in zip(resultat, attendu):
    assert sont_proches(x, y), f"Erreur avec {x} qui n'est pas proche de {y} dans arange(5.0, 6.5, 0.25)"

assert arange(2.0, 2.0, 0.1) == [], "Générer un nombre entre 2 inclus et 2 exclus renvoie un tableau vide."
