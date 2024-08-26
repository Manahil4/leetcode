n8=int( input("number to repeat pattern" ))
row=1
col=1
for row in range(1,n8+1) :

    for col in range (1,row+1 ):
        print  (row, end="" )
        col += 1
    print()
    row +=1
