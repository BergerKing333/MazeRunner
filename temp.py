def iterative_power(a, n):
    result = 1  # Initialize result to 1
    base = a
    print(a**n)
    while n > 0:
        print(result * (base**n))
        if n % 2 == 1:
            result *= base
            n -= 1
        else:
            base *= base
            n //= 2 
        
    return result

print(iterative_power(2, 9))  # 8