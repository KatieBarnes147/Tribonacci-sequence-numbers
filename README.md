# Tribonacci-sequence-numbers
# Tribonacci Sequence Calculator
A simple Python program that interactively computes the nᵗʰ Tribonacci number.  
The Tribonacci sequence works like the Fibonacci sequence, but each term is the sum of the **three** preceding terms:
T₀ = 0,
T₁ = 1,
T₂ = 1,
Tₙ = Tₙ₋₁ + Tₙ₋₂ + Tₙ₋₃ for n ≥ 3

## Prerequisites

- Python 3.6 or higher

## Usage

1. Open a terminal/command prompt.  
2.  ```bash
  python BarnesKatieProject3.py
3. Follow the on-screen prompt:
Enter a positive integer (or a non-positive integer to exit):
4. Input your desired n and press Enter. The program will display:
The nᵗʰ element of the Tribonacci sequence is: X
5. Enter a non-positive integer (e.g. 0 or -1) to terminate.

Example Session
Enter a positive integer (or a non-positive integer to exit): 6
The 6ᵗʰ element of the Tribonacci sequence is: 9

Enter a positive integer (or a non-positive integer to exit): 9
The 9ᵗʰ element of the Tribonacci sequence is: 57

Enter a positive integer (or a non-positive integer to exit): 0
Exiting the program.

How It Works
The program maintains the last three Tribonacci values in variables (or a list) and iteratively builds up to the nᵗʰ term in O(n) time.

Input is validated to ensure only integers are processed, and the loop exits cleanly on a non-positive integer.


