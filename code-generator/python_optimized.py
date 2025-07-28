
import time

# Use memoization to improve the performance of the Fibonacci calculation
def fibonacci_recursive(n, memo):
    if n <= 1:
        return n
    if memo[n] != 0:
        return memo[n]
    memo[n] = fibonacci_recursive(n - 1, memo) + fibonacci_recursive(n - 2, memo)
    return memo[n]

def print_fibonacci_recursive(count):
    print("Fibonacci Series (Recursive):")
    memo = [0] * (count + 1)
    for i in range(count):
        print(fibonacci_recursive(i, memo), end=" ")
    print()

def main():
    count = 10
    memo = [0] * (count + 1)  # Initialize memoization array
    start_time = time.time()
    fibonacci_recursive(count, memo)
    end_time = time.time()
    print("Execution Time: {:.6f} seconds".format(end_time - start_time))

if __name__ == "__main__":
    main()

