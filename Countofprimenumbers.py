def isPrime(n):
    primeCount =0
    for num in range(2,n+1):
        for i in range(2,num):
            if num%i ==0:
                break            
        else:
            primeCount += 1

    return primeCount

print(isPrime(100000));