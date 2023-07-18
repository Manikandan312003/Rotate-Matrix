def rotateMatrix(arr):      #90 degree
    arr=list(zip(*arr))
    arr=[i[::-1] for i in arr]
    return arr

row,clm=map(int,input().split())
arr=[]
for i in range(row):
    print('')       #Bug Not get input
    arr.append(list(map(int,input('').split())))
print(rotateMatrix(arr))

