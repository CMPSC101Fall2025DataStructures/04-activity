"""
Square Root Approximator - STUDENT VERSION
CS101 Fall 2025 - Activity 04

This program uses Newton's method to approximate square roots using while loops
and conditional statements for mathematical computation.

INSTRUCTIONS: Look at the error messages when you try to run the program. Python will tell you 
             exactly which functions it can't find. Then check what functions are actually
             defined in math_approximator.py (open that file and look at the function names).
             
             If you see "NameError: name 'some_function' is not defined", it means the
             import statement doesn't match the actual function name in the other file.
"""

# TODO 1: Fix the import statement - what's missing?
# HINT: You need to import the 'math' module for mathematical functions like math.sqrt()
import math

# TODO 2: This import has an error - fix the function names
# HINT: Compare these names with the actual function names in math_approximator.py
# Look for functions that start with similar letters but have different names
from math_approximator import newton_sqrt_calculator, input_validator, guess_starter


def get_positive_number():
    """Get a positive number from user with validation."""
    while True:
        try:
            # TODO 3: Fix this input prompt - make it more clear what the user should enter
            # HINT: The current prompt "Enter number:" is too vague. Users might not know
            #       what kind of number to enter. Make it specific like "Enter a positive number:"
            number = float(input("Enter number: "))
            
            # TODO 4: Add proper error handling - what should happen if number <= 0?
            # HINT: When the user enters a negative number or zero, we print an error message
            #       but then the function continues to the 'else' clause and returns the bad number!
            #       You need to add a 'continue' statement to go back to the beginning of the loop.
            if number <= 0:
                print("Error: Please enter a positive number.")
                # Missing continue statement - student needs to add this
            else:
                return number
                
        except ValueError:
            # TODO 5: Make this error message more helpful
            # HINT: "Error!" doesn't tell the user what they did wrong. Be more specific!
            #       Tell them they need to enter a valid number, not text or symbols.
            print("Error!")


def get_tolerance():
    """Get desired precision/tolerance from user."""
    # TODO 6: This function has a logic error in the range checking
    # HINT: Look at the condition "if 0 > tolerance > 1:" - this is impossible!
    #       No number can be both greater than 0 AND greater than 1 at the same time.
    #       What should the condition be? Think: tolerance should be a small positive number
    #       between 0 and 1 (like 0.001 or 0.0001).
    while True:
        try:
            tolerance = float(input("Enter desired precision (e.g., 0.0001): "))
            # BUG: This condition is wrong - what's the correct range?
            if 0 > tolerance > 1:
                return tolerance
            else:
                print("Error: Tolerance should be between 0 and 1.")
        except ValueError:
            print("Error: Please enter a valid number.")


def get_max_iterations():
    """Get maximum number of iterations from user."""
    while True:
        try:
            max_iter = int(input("Enter maximum iterations (default 100): ") or "100")
            if max_iter > 0:
                return max_iter
            else:
                print("Error: Please enter a positive integer.")
        except ValueError:
            print("Error: Please enter a valid integer.")


def compare_with_builtin(number, approximation):
    """Compare our approximation with Python's built-in sqrt function."""
    # TODO 7: Create a dictionary called 'results' to store all the comparison data
    # HINT: A dictionary uses curly braces {} and stores key-value pairs like:
    #       my_dict = {'key1': value1, 'key2': value2}
    # It should have keys: 'our_result', 'builtin_result', 'absolute_error', 'relative_error'
    # You can create it after calculating all the values below.
    
    builtin_sqrt = math.sqrt(number)
    error = abs(approximation - builtin_sqrt)
    relative_error = (error / builtin_sqrt) * 100 if builtin_sqrt != 0 else 0
    
    # TODO 8: Instead of separate print statements, use a list to store the information
    # HINT: Create a list like: info_lines = ["line1", "line2", "line3", ...]
    # and then iterate through it to print each line with a for loop: for line in info_lines:
    print(f"\n=== Comparison with Built-in Function ===")
    print(f"Our approximation:     {approximation:.10f}")
    print(f"Python's math.sqrt():  {builtin_sqrt:.10f}")
    print(f"Absolute error:        {error:.2e}")
    print(f"Relative error:        {relative_error:.6f}%")
    
    # TODO 9: Return the results dictionary you created above
    # HINT: Add a return statement with your dictionary: return results


def demonstrate_convergence():
    """Demonstrate how Newton's method converges for different starting points."""
    print("\n=== Convergence Demonstration ===")
    test_number = 25.0
    
    # TODO 10: Create a list called 'starting_points' with values: [1.0, 10.0, 50.0, 100.0]
    # HINT: A list uses square brackets [] and separates items with commas:
    #       my_list = [item1, item2, item3, item4]
    #       Make sure to use decimal numbers (1.0 not 1) to match the rest of the code.
    
    print(f"Computing sqrt({test_number}) with different starting points:")
    print(f"Target: {math.sqrt(test_number):.6f}")
    print("-" * 60)
    
    # TODO 11: Write a for loop to iterate through starting_points
    # HINT: Use this pattern: for variable_name in list_name:
    #       Inside the loop, call newton_sqrt_calculator with each starting point
    # For each starting point, call newton_sqrt_calculator and print results
    # Use this format: f"Start: {start:6.1f} → Result: {result:.6f} (in {iterations:2d} iterations)"
    # 
    # Example structure:
    # for start in starting_points:
    #     result, iterations, converged = newton_sqrt_calculator(test_number, ...)
    #     if converged:
    #         print(f"Start: {start:6.1f} → Result: {result:.6f} (in {iterations:2d} iterations)")
    #     else:
    #         print(f"Start: {start:6.1f} → Failed to converge in {iterations} iterations")


def main():
    """Main program function."""
    print("=== Newton's Method Square Root Approximator ===")
    print("This program approximates square roots using Newton's iterative method.")
    print()
    
    while True:
        print("\nOptions:")
        print("1. Calculate square root")
        print("2. Show convergence demonstration")
        print("3. Batch calculation")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == '1':
            # Single calculation
            number = get_positive_number()
            tolerance = get_tolerance()
            max_iterations = get_max_iterations()
            
            print(f"\nCalculating sqrt({number}) with tolerance {tolerance}...")
            print("-" * 50)
            
            # Get initial guess
            # TODO 12: Fix this function call - check the import statement for the correct name
            # HINT: Look at the import statement at the top of the file. What function names did you import?
            #       The function should be called 'guess_starter' based on the import, not 'initial_guess'
            guess = guess_starter(number)
            print(f"Initial guess: {guess}")
            
            # Perform Newton's method
            # TODO 13: Fix this function call - use the correct imported function name
            # HINT: Again, check the import statement. The main calculation function should be
            #       'newton_sqrt_calculator', not 'newton_sqrt'
            result, iterations, converged = newton_sqrt_calculator(
                number, tolerance, max_iterations, guess, show_steps=True
            )
            
            if converged:
                print(f"\n✓ Converged after {iterations} iterations")
                print(f"Final approximation: {result:.10f}")
                
                # Compare with built-in function
                compare_with_builtin(number, result)
            else:
                print(f"\n✗ Failed to converge within {max_iterations} iterations")
                print(f"Last approximation: {result:.10f}")
        
        elif choice == '2':
            # Show convergence demonstration
            demonstrate_convergence()
        
        elif choice == '3':
            # Batch calculation
            print("\n=== Batch Square Root Calculation ===")
            numbers_input = input("Enter numbers separated by spaces: ")
            
            try:
                numbers = [float(x) for x in numbers_input.split()]
                tolerance = get_tolerance()
                
                print(f"\nCalculating square roots with tolerance {tolerance}:")
                print("-" * 70)
                print(f"{'Number':<12} {'Approximation':<15} {'Built-in':<15} {'Iterations':<12}")
                print("-" * 70)
                
                # TODO 14: Create a dictionary called 'test_results' to store results for each number
                # HINT: You can create an empty dictionary like: test_results = {}
                # Then inside the loop below, you can add entries like: 
                # test_results[num] = {'number': num, 'approximation': result, 'builtin': builtin, 'iterations': iterations, 'converged': converged}
                # Keys should be: 'number', 'approximation', 'builtin', 'iterations', 'converged'
                
                for num in numbers:
                    if num > 0:
                        # TODO 15: Fix this function call
                        # HINT: Use the same function name as in the import statement: 'newton_sqrt_calculator'
                        result, iterations, converged = newton_sqrt_calculator(
                            num, tolerance, max_iterations=100
                        )
                        builtin = math.sqrt(num)
                        
                        if converged:
                            print(f"{num:<12.3f} {result:<15.6f} {builtin:<15.6f} {iterations:<12d}")
                        else:
                            print(f"{num:<12.3f} {'Failed':<15} {builtin:<15.6f} {'>100':<12}")
                    else:
                        print(f"{num:<12.3f} {'Invalid (≤0)':<15} {'N/A':<15} {'N/A':<12}")
                        
                # TODO 16: Add a print statement showing the total number of numbers processed
                # HINT: You can get the length of a list with len(list_name)
                # Print something like: f"Processed {len(numbers)} numbers total."
                        
            except ValueError:
                print("Error: Please enter valid numbers.")
        
        elif choice == '4':
            print("Thank you for using the Square Root Approximator!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()