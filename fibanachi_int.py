def fib_memoize(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_memoize(n - 1, d) + fib_memoize(n - 2, d)
        d[n] = ans
        return ans
base_case = {0: 1, 1: 1}

print(fib_memoize(12, base_case))