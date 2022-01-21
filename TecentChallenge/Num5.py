re=0
def con(conj:str,connection:int):
    if(connection==1):
        conj+="+"
    if (connection == 2):
        conj += "-"
    if (connection == 3):
        conj += "*"
    if (connection == 4):
        conj += "/"
    return  conj
golbalconj=""
for a in range(1,5):
    for b in range(1, 5):
        for c in range(1, 5):
            for d in range(1, 5):
                for e in range(1, 5):
                    for f in range(1, 5):
                        for g in range(1, 5):
                            for h in range(1, 5):
                                golbalconj="1.0"
                                golbalconj=con(golbalconj,a)
                                golbalconj+="2.0"
                                golbalconj = con(golbalconj,b)
                                golbalconj+="3.0"
                                golbalconj=con(golbalconj,c)
                                golbalconj+="4.0"
                                golbalconj = con(golbalconj,d)

                                golbalconj+="5.0"
                                golbalconj = con(golbalconj,e)

                                golbalconj+="6.0"
                                golbalconj = con(golbalconj,f)

                                golbalconj+="7.0"
                                golbalconj = con(golbalconj,g)

                                golbalconj+="8.0"
                                golbalconj=con(golbalconj,h)

                                golbalconj+="9.0"
                                re=eval(golbalconj)
                                if(abs(re+497)<=0):
                                    print(golbalconj)
                                    print(re)