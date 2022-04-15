def renverser(mot):
    t = ''
    for i in range(len(mot)) :
        t += mot[-i-1]
    return t

# Tests
renverser('informatique') == 'euqitamrofni'
renverser('nsi') == 'isn'
renverser('') == ''
