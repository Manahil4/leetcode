n8=int( input("number to repeat pattern" ))

res=[[1]]
temp=[]
for row in range(1,n8+1) :
    rowl=[]
    temp=[0]+res[-1]+[0]
    for col in range (len(res[-1])+1 ):
        rowl.append(temp[col]+temp[col+1])
    res.append(rowl)
return res
