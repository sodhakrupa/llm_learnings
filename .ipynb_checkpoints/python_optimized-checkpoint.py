
import time

# Use memoization to improve the performance of the Fibonacci calculation
memo = {}

def fibonacci_recursive(n):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    return memo[n]

def print_fibonacci_recursive(count):
    print("Fibonacci Series (Recursive):")
    for i in range(count):
        print(fibonacci_recursive(i), end=" ")
    print()

if __name__ == "__main__":
    count = 10
    # Initialize memoization dictionary
    start_time = time.time()
    fibonacci_recursive(count)
    end_time = time.time()
    duration = end_time - start_time
    print(f"Execution Time: {duration:.6f} seconds")

