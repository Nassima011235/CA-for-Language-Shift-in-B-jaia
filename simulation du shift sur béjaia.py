# Créé par Nassima, le 16/07/2023 en Python 3.7
import numpy as np
from pylab import *
import cv2
import matplotlib.pyplot as plt
import random
import matplotlib.patches as mpatches

#Afficher la carte intiale.

img=cv2.imread('Bejaia.jpg')
plt.imshow(img)
plt.show()

#clustring de la carte intiale en deux couleur.
img2=img.reshape((-1,3))
img2=np.float32(img2)
criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
k=2
attempts=10
ret,label,center=cv2.kmeans(img2,k,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)
center=np.uint8(center)
res=center[label.flatten()]
res2=res.reshape((img.shape))

print(center)


#creation de la carte intiale avec despourcenatge appropriés.

A=np.zeros((res2.shape[0]+1,res2.shape[1]+1))
for i in range(res2.shape[1]):
   for j in range(res2.shape[0]):
       
         if all(res2[j][i]==[184,223,249]):
            res2[j][i]=[255,255,255]
            A[j][i]= 4
         elif all(res2[j][i]==[253,254,254]):
            
            my_list = ['3'] *17  + ['2'] * 23 +['1'] *20 + ['0'] * 40
            A[j][i]=int(random.choice(my_list))
            if A[j][i]==3:
                res2[j][i]= [0,0,0] #noir
            elif A[j][i]==2:
                res2[j][i]= [0,0,225] #blue
            elif A[j][i]==1:
                res2[j][i]= [225,0,0] #red
            elif A[j][i]==0: 
                res2[j][i]= [225,225,0] #yellow
                
       
        
#affichage de la carte intiale.
color_patch1 = mpatches.Patch(color='yellow', label='state 0')
color_patch2= mpatches.Patch(color='red', label='state 1')
color_patch3= mpatches.Patch(color='blue', label='state 2')
color_patch4= mpatches.Patch(color='black', label='state 3')
plt.legend(handles=[color_patch1, color_patch2, color_patch3, color_patch4],prop={"size": 8}, loc="best")
plt.imshow(res2)
plt.show()
cv2.imwrite('Bejaia_entree.jpg',res2)

#choix des paramètres et nombre d'itérations.
Pe=3
Pz=3
n=1
k=1
while k<=n:
    for i in range(res2.shape[1]):
       for j in range(res2.shape[0]):
           if A[j][i] != 4:
               north=int(A[j][i+1])
               south=int(A[j][i-1])
               ouest=int(A[j+1][i])
               est=int(A[j-1][i])
               if north != 4:
                   a=int(north/2)
                   a1=int(north-north/2)                  
               else: 
                   a=0
                   a1=0
                   
               if south != 4:
                   b=int(south/2)
                   b1=int(south-south/2)
               else: 
                   b=0
                   b1=0
                   
               if est != 4:
                   c=int(est/2)
                   c1=int(est-est/2)
               else: 
                   c=0
                   c1=0
                   
               if ouest != 4:
                   d=int(ouest/2)
                   d1=int(ouest-ouest/2)
               else:
                   d=0
                   d1=int(ouest-ouest/2)
              
               sum0=a+b+c+d
               sum1=a1+b1+c1+d1
               
               if (A[j][i]==0) and (int(sum0) >= Pz) and (int(sum1) >=Pe):
                   A[j][i]=3
               elif (A[j][i]==1) and (int(sum0) >= Pz):
                   A[j][i]=3
               elif (A[j][i]==2) and (int(sum1) >=Pe):
                   A[j][i]=3
               elif (A[j][i]==0) and (int(sum0) >= Pz) and (int(sum1) < Pe):
                   A[j][i]=2
               elif (A[j][i]==0) and (int(sum0) <= Pz) and (int(sum1) >=Pe):
                   A[j][i]=1
               else: A[j][i]=A[j][i]
    
           
                   
    for i in range(res2.shape[1]):
       for j in range(res2.shape[0]):
             if A[j][i]==3:
                res2[j][i]=[0,0,0]              
             elif A[j][i]==2:
                    res2[j][i]= [0,0,225] 
             elif A[j][i]==1:
                    res2[j][i]= [225,0,0] #red
             elif A[j][i]==0: 
                 res2[j][i]= [225,225,0] #yellow
             elif A[j][i]==4:
                 res2[j][i]= [225,225,225]
    color_patch1 = mpatches.Patch(color='yellow', label='state 0')
    color_patch2= mpatches.Patch(color='red', label='state 1')
    color_patch3= mpatches.Patch(color='blue', label='state 2')
    color_patch4= mpatches.Patch(color='black', label='state 3')
    plt.legend(handles=[color_patch1, color_patch2, color_patch3, color_patch4],prop={"size": 8}, loc="best")
                
    plt.imshow(res2)
    plt.show()
    k=k+1





color_patch1 = mpatches.Patch(color='yellow', label='state 0')
color_patch2= mpatches.Patch(color='red', label='state 1')
color_patch3= mpatches.Patch(color='blue', label='state 2')
color_patch4= mpatches.Patch(color='black', label='state 3')
plt.legend(handles=[color_patch1, color_patch2, color_patch3, color_patch4],prop={"size": 8}, loc="best")
                
plt.imshow(res2)
plt.show()
cv2.imwrite('resultat shift.jpg',res2)
