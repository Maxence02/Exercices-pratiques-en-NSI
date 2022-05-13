def recherche(elt, tab) :
    o = -1
    for i in range (len(tab)) :
        if elt == tab[i] :
            o = i
    return o
            
print (recherche(1, [2, 3, 4]))
print (recherche(1, [10, 12, 1, 56]))
print (recherche(50, [1, 50, 1]))
