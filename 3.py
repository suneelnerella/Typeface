lis = [0,1,2,5,6,8,9]
def valid(n):
    for i in str(n):
        if int(i) not in lis:
            return False
    return True

def led_display(num):
    result=0
    if num<8:
        return lis[num-1]
    dummy,n=7,10
    while dummy<=num:
        if(valid(n)):
            result = n
            dummy+=1
        n+=1
    return result
num = int(input())

print(led_display(num))