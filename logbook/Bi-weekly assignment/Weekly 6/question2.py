def factors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

# Test
print(factors(12))   # [1, 2, 3, 4, 6, 12]