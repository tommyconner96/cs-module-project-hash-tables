
cache = {}

def fib(n):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]

    # if result is not in cache
    # do expensive calculations below    
    result = fib(n-1) + fib(n-2)

    cache[n] = result

    return result

# print(fib(5)) # 5
print(fib(998)) # 13
print(cache)
