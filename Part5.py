def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False, i
    return True, None


x = int(input("x: "))

prime, divisor = is_prime(x)
if prime:
    print(f"{x} adad aval mibashad")
else:
    print(f"{x} adad aval nmibashad. maqsoam alayih: {divisor}")
