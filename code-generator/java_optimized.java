
public class FibonacciRecursive {

    // Memoization for optimized recursive calls
    private static long[] memo;

    private static long fibonacciRecursive(int n) {
        if (n <= 1) return n;
        if (memo[n] != -1) return memo[n];
        memo[n] = fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
        return memo[n];
    }

    private static void printFibonacciRecursive(int count) {
        System.out.println("Fibonacci Series (Recursive):");
        for (int i = 0; i < count; i++) {
            System.out.print(fibonacciRecursive(i) + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int count = 10;
        memo = new long[count + 1];
        
        // Initializing memoization array
        for (int i = 0; i < memo.length; i++) {
            memo[i] = -1;
        }

        long startTime = System.nanoTime();
        printFibonacciRecursive(count);
        long endTime = System.nanoTime();
        
        System.out.printf("Execution Time: %.6f seconds%n", (endTime - startTime) / 1_000_000_000.0);
    }
}
