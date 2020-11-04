s=''
for q in range(1,10):
    for l in range(1,4):
        for c in range(1,4):
            print("Quadrante %d Linha %d Coluna %d"%(q,l,c))
            n=input()
            n=int(n)
            if(n!=0):
                s+=("%d_P_%d_%d_Q_%d\n"%(n,l,c,q))

arq = open('arq3.txt', 'w')
arq.write(s)
arq.close()
0
