str1=input()
str2=input()
last_char=str2[-1]
count=0
for i in str1:
    if last_char==i:
        count+=1
print(count)
