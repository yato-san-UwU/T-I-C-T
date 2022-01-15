print("voici le regrouprment de tout les TP precedents")
print("                *********AVERTISSEMENT*********")
print("il est suppose que l'utilisateur lui meme prenne en compte que la somme de P=1")
print("")

print("1.TP entropie dune source")
print("2.TP entropie de 2 source")
print("3.TP source independante")
print("4.TP quantité d'information mutuelle")
print("5.TP entropie conditionelle")
print("6.TP code prefixe")
print("7.TP code huffman/shanon")

print("")
U=input("entrer le numero de la fonction que vous voulez executer :")
U=int(U)
print("\n")

if U==1:            #("1.TP entropie dune source")
    from math import log

    nbr=input("entrer le nombre de probabiliter :")
    nbr = int(nbr)
    H=0

    prb = []
    for i in range(nbr):
        prb.append(float(input("Entrer la probabiliter :")))

    for k in range(nbr):
        H=prb[k]*math.log2(1/prb[k])+H

    print("lentropie d'une source est :  ", H)


elif U==2:      #("2.TP entropie de 2 source")
    import math
    from math import log    

    N=input('Donnez la taille de la premier source :')
    M=input('Donnez la taille de la deuxiemme source :')

    N = int(N)
    M = int(M)

    ttl= N*M

    H=0

    p=[]

    for i in range(N):
        for j in range(M):
            p.append(float(input("Donnez les probabilite p(x,y) :")))
            
    for k in range(ttl):
        H=p[k]*math.log2(1/p[k])+H

    print("l'entropie H(X,Y) de deux source est = ", H)

elif U==3:              #("3.TP source independante")
    from math import log


    nbr1=input("entrer le nombre de probabiliter de la source 1 p(x) :")
    nbr2=input("entrer le nombre de probabiliter de la soucre 2 p(y) :")
    nbr1 = int(nbr1)
    nbr2 = int(nbr2)

    H1=0
    H2=0

    prb1 = []
    for i in range(nbr1):
        prb1.append(float(input("Entrer les probabiliter de la source 1 p(x) :")))

    for k in range(nbr1):
        H1=prb1[k]*log(1/prb1[k])+H1

    print("lentropie de la premier source H(X) est :", H1)

            #-------------------------------------------------------------------

    prb2 = []
    for i in range(nbr2):
        prb2.append(float(input("Entrer les probabiliter de la source 2 p(y):")))

    for k in range(nbr2):
        H2=prb2[k]*log(1/prb2[k])+H2

    print("lentropie de la deuxiemme source H(Y) est :", H2)

    H=H1+H2
    print(" H(X,Y) = H(X)+H(Y) = ",H)

elif U==4:              #("4.TP quantité dinformation mutuelle")
    import math
    from math import log

    X=input('Donnez le nombre de probabiliter X de la premier source : ')
    Y=input('Donnez le nombre de probabiliter Y de la deuximme source : ')
    X = int(X)
    Y = int(Y)
    ttl= X*Y

    HX=0            #entropie Hx
    HY=0            #entropie Hy
    Ixy=0           # Ixy
    Hxy=0           #entropie generale

    pxy=[]          #probabiliter pxy
    px=[]           #probabiliter px
    py=[]           #probabiliter py


    for i in range(X):
        px.append(float(input('Donnez les probabilite p(x) :')))
        
    for k in range(X):
        HX=px[k]*math.log2(1/px[k])+HX

            #----------- PX
        
    for i in range(Y):
        py.append(float(input("Donnez les probabiliter p(y) :")))
        
    for k in range(Y):
        HY=py[k]*math.log2(1/py[k])+HY

            #----------- PY

    for i in range(X):
        for j in range(Y):
            pxy.append(float(input("Donnez les probabilite  p(x,y) :")))        
            
            #----------- PXY
            
    for i in range(ttl):
        Hxy=pxy[i]*math.log2(1/pxy[i])+Hxy

    Ixy=HX+HY-Hxy
    print("\n")
    print(" H(X) =",HX)
    print(" H(Y) =",HY)
    print(" H(X,Y) = ",Hxy)
    print("")
    print(" on a H(X,Y)=H(X)+H(Y)-I(xy)")
    print(" ce qui fait que I(xy)= H(X)+H(Y)-H(X,Y)")
    print(" Ixy =",Ixy)
        
elif U==5:              #("5.TP entropie conditionelle")
    import math
    from math import log

    N=input("donnez la taille de la source X :")
    M=input("donnez la taimme de la source Y :")
    N=int(N)
    M=int(M)

    T=N*M

    pxy=[]          #probabiliter X sachant y
    Hxy=0           #entropie conditionnel
    py=[]           #probabiliter y
    sompy=0         #somme de p(y)
    hxymoy=0        #entropie conditonnelle moyenne

    for i in range(N):
        for j in range(M):
            pxy.append(float(input("donnez les probabiter p(x|y) :")))
            
    for i in range(T):
        Hxy=pxy[i]*math.log2(1/pxy[i])+Hxy
        
    print("lentropie conditionelle H(X|y)=",Hxy)


    for i in range(M):
        py.append(float(input("donnez les probabiliter p(y) :")))
        
    for i in range(M):
        sompy=py[i]+sompy

    hxymoy=sompy*Hxy

    print("lentropie conditionnelle moyenne H(X|Y)=",hxymoy)

elif U==6:              #("6.TP code prefixe")
    H=input("entrer le nombre de code :")
    H=int(H)
    print("")
    print("*****avertissment*****")
    print("il est demander a l'utilisateur de rentrer les code de manierre croissant")
    print("selon leur longueure exemple :")
    print("pour '01,111,10,1' vous devez entrer '1,01,10,111' ")
    print("pour '123,34,4567,89' vous devez entrer '34,89,123,4567' ")
    print("")

    tab=[]
    decomposition=0
    decomposition2=0     #nombre quon utilise pour comparé
    tab2=[]
    tab3=[]
    aide=0
    for i in range(H):
            tab.append(str(input("entrer les codes :")))           
    
    d=int(0)
    m=int(0)
    ZSQ=1
    for i in range(H-1):
        for j in range(i+1,H):
         d=len(tab[i])
         m=len(tab[j])
         if ZSQ==1:
            if d!=m:
               decomposition = str(tab[j])
               decomposition2= str(tab[i])
               for h in range(d):
                     tab2.append(0)
                     tab3.append(0)
                      
               for q in range(d):
                  tab2[0]=decomposition2[q]
                  tab3[0]=decomposition[q]                  
               if ZSQ==1:
                  if tab2[0]==tab3[0]:
                     ZSQ=0
                  else:
                     ZSQ=1
            elif d==m:
               if tab[i]==tab[j]:
                  ZSQ=0
               else:
                  ZSQ=1
                        
    if ZSQ==0:
        print("le code nest pas prefixe")
    else:
        print("le code est prefixe")                          
   
elif U==7:              #("7.TP code huffman/shanon")
    print("ce code presente le trie selon huffman et le codage selon shanon")
    N=input("\nentrez le nombre de probabiliter :")
    N =int(N)
    nbr=N

    prob=[]     #les proba
    aide=0
    tab2=[]

    nvl=N       #recupere la taille du nouveau tableau


    for v in range(N):
        prob.append(float(input("Donnez les probabilite P(x): ")))

    for D in range(N-2):    
        for v in range(nvl):
            for i in range(nvl-1):
                if prob[i]<prob[i+1]:
                    aide=prob[i+1]
                    prob[i+1]=prob[i]
                    prob[i]=aide
                        
        print('\ntableau N°',D,'trié',prob)         #boucle tri du tableau

        prob[nvl-2]=prob[nvl-2]+prob[nvl-1]
        del prob[nvl-1]                   #somme des deux derniere valeur

        print('tableau N°',D,'apres la somme',prob)
        
        nvl=len(prob)           #recupere la valeur du nouveau tableau

        for v in range(nvl):
            for i in range(nvl-1):
                if prob[i]<=prob[i+1]:
                    aide=prob[i+1]
                    prob[i+1]=prob[i]
                    prob[i]=aide
                    
        print("le tableau ",D," apres la somme et le trie ",prob)                 #boucle tri avec les nouvelles valeur
    
    shanon=[]
    for i in range(N):
        shanon.append(0)
        
    shanon[0]=0
    shanon[1]=10
    b=100

    for i in range(2,N):
        if i<N-1:
            shanon[i]=shanon[i-1]+b
            b=b*10
        if i==N-1:
                shanon[i]=shanon[i-1]+1

    print("codage selon shanon :")
    for i in range(N):
        print('les proba :',tab2[i],' son code: ',shanon[i])
    
else:
    print("numero non valide")