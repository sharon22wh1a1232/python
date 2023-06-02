m1=[[1,2,3],
        [4,5,6],
        [7,8,9]]
m2=[[9,8,7],
        [6,5,4],
        [3,2,1]]
m3=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range (len(m1)):
    for k in range(len(m2)):
        m3[i][k]=m1[i][k]+m2[i][k]
print("the sum of matrix m1 and m2= ",m3)
