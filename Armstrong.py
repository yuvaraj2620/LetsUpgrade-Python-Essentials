lower =1042000
upper = 702648265
for num in range (lower, upper + 1):
    o= len (str(num))
    sum = 0
    temp = num
    while temp > 0:
        x = temp % 10
        sum += x ** o
        temp //= 10

    if num == sum:
        print(num)
        break