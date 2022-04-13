from time import perf_counter

start = perf_counter()
primes = [1, 2, 3] + [i for i in range(5, 1000000) if i % 6 == 5 or i % 6 == 1 and i % 5 != 0 and i % 3 != 0 and i % 7 != 0]
end = perf_counter()
print((end - start))