def supprimheu(mots):
    t = ''
    for i in mots :
        if i != 'heu' :
            if t != '' :
                t += ' '
            t += i
    return t

# tests

assert supprimheu(["je", "heu", "vais", "coder", "heu", "la",
 "fonction", "supprimheu"]) == 'je vais coder la fonction supprimheu'

assert supprimheu(["c", "est", "facile"]) == 'c est facile'
