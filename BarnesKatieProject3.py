def tribonacci(n):
    # Handle the base cases
    if n == 1 or n == 2 or n == 3:
        return 1
    
    # Use a list to store computed values for dynamic programming
    trib = [0] * (n + 1)
    trib[1], trib[2], trib[3] = 1, 1, 1
    
    # Compute the Tribonacci numbers up to n
    for i in range(4, n + 1):
        trib[i] = trib[i - 1] + trib[i - 2] + trib[i - 3]
    
    return trib[n]

def main():
    while True:
        user_input = input("Enter a positive integer (or a non-positive integer to exit): ")
        try:
            n = int(user_input)
            if n < 1:
                print("Exiting the program.")
                break
            result = tribonacci(n)
            print(f"The {n}-th element of the Tribonacci sequence is: {result}")
        except ValueError:
            print("Please enter a valid positive integer.")

if __name__ == "__main__":
    main()
    
input("Press Enter to close the program.")
