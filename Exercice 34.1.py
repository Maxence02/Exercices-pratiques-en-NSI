alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def occurrence_max(chaine) :
    mx = 0
    
    for i in range(len(alphabet)) :
        n = 0
        for l in range(len(chaine)) :
            if alphabet[i] == chaine[l] :
                n += 1
                if n > mx :
                    mx = n
                    lettre = chaine[l]
        
        
    return lettre 
        
ch = 'je suis en terminale et je passe le bac et je souhaite poursuivre des etudes pour devenir expert en informatique'
print(occurrence_max(ch))
