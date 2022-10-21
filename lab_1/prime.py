def prime(num):
    for i in range(2, int(num / 2)):
        if (num % i) == 0:
            return False
    return True


def select_primes(array):
    return list(filter(lambda num: prime(num), array))


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(prime(3))
print(select_primes(arr))
