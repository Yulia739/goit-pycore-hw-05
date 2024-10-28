def caching_fibonacci():
    # Initializes the cache and returns the internal function fibonacci
    cache = {}

    def fibonacci(n):
        # Calculates the Fibonacci number using the cache.
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    return fibonacci


fibonacci = caching_fibonacci()

# Use the fibonacci function to calculate Fibonacci numbers
print(fibonacci(48))
