def prime_num(n):
    if n>1:
        for i in range (2,n):
            if n%i==0:
                return False
        return True
lst_prime=list(filter(prime_num,range(1,2500)))
print(len(lst_prime))