def contador(lts):
    ord = lts.sort()
    tamanho = len(lts)
    mat = []
    for z in range(tamanho)
        mat += [0]
    rep = 0
    ind = 0
    while rep < tamanho:
        if ord[rep] == ord[rep+1]:
            cont = 0
            while ((ord[rep] == ord[rep+1]) and (rep<tamanho)):
                cont+=1
                mat[ind]=cont
                rep+=1
            rep+=1
            ind+=1
        else:
            mat[ind]

    while 0 in mat:
        mat.remove(0)