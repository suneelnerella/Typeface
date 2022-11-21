def decimal_to_base3(num):
    result=""
    sign = "-" if num<0 else ""
    num = abs(num)
    if num<3:
        return num
    while num:
        result = str(num%3)+result
        num //=3
    return sign+result




decimal = int(input())
print(decimal_to_base3(decimal))
