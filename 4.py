arr=[list(map(int,input().split())) for _ in range(4)]
row1,row2 = 0,len(arr)-1
c1,c2=0,len(arr[0])-1
if(arr[row1][0]!=0):
    row1+=1
if arr[row2][0]!=0:
    row2-=1
if arr[0][c1]!=0:
    c1+=1
if arr[0][c1]!=0:
    c2-=1

print(row1,c1)
print(row1,c2)
print(row2,c1)
print(row2,c2)