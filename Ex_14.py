matrice=[]
n=int(input("Dați dimensiunea matricei de la 2 pina la 10:"))
if n>=2 and n<=10:
  for i in range(0,n):
    k=list(eval(input("Dați elementele:")))
    matrice.append(k)
   
print(*matrice, sep='\n')


d_p=[]
for i in range(len(matrice)):
    for j in range(len(matrice[0])) :
        if i==j :
            d_p.append(matrice[i][j])
print("Suma pe diagonala principală:",sum(d_p))

d_s=[] 
for i in range(len(matrice)):
    for j in range(len(matrice[0])) :
        if i+j==n-1:
            d_s.append(matrice[i][j])
print("Suma diagonala secundară:",sum(d_s)) 

m_s_d_p=[]
for i in range(len(matrice)):
    for j in range(len(matrice[0])) :
        if i-j<0 :
            m_s_d_p.append(matrice[i][j])
print("Suma mai sus de diagonala principală:",sum(m_s_d_p))

m_j_d_p=[]
for i in range(len(matrice)):
    for j in range(len(matrice[0])) :
        if i-j>0 :
            m_j_d_p.append(matrice[i][j])
print("Suma mai jos de diagonala principală:",sum(m_j_d_p))

m_s_d_s=[]
for i in range(len(matrice)):
    for j in range(len(matrice[0])) :
        if i+j<n-1 :
            m_s_d_s.append(matrice[i][j])
print("Suma mai sus de diagonala secundară:",sum(m_s_d_s))

m_j_d_s=[]
for i in range(len(matrice)):
    for j in range(len(matrice[0])) :
        if i+j>n-1 :
            m_j_d_s.append(matrice[i][j])
print("Suma mai jos de diagonala secundară:",sum(m_j_d_s))
