# from sys import 

def flag(i,col) :
    
    k =0
    flag = True
    while k<i and flag :
        if col[i] == col[k] or abs(col[i]-col[k]) == i-k :
            flag = False
        k+=1
    return flag
def n_queen (i,col) :
     if flag(i,col) :
        if i == len(col)  :
            print (col)
        else :
            for j in range(0, i)  :
                col[i] = j
                n_queen(i+1,col)
n =8           
col = [0] * n
 
for i in range(n) :
    n_queen(i,col)   