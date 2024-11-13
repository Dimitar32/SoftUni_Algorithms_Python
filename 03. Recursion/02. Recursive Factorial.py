def cal_fac(num):
    if num == 1:
        return 1
    return num * cal_fac(num - 1)

num = int(input())

print (cal_fac(num))