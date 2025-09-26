"""
Math Approximator Module - STUDENT VERSION
CS101 Fall 2025 - Activity 04

This module implements Newton's method for square root approximation using
while loops, conditionals, and mathematical algorithms.

TODO 17: Add any missing import statements that might be needed
HINT: This module uses mathematical functions like sqrt(). What module do you need to import?
      Look at the functions below - do you see any that start with "math."?

TODO 18: Check all function names - make sure they match what main.py is expecting
HINT: Open main.py and look at the import statement. The function names in this file
      must exactly match what main.py is trying to import. If there's a mismatch,
      you'll get "ImportError: cannot import name" errors.
"""

# TODO 19: Are there any imports missing? Check what functions from math module we use
# HINT: Look through this file for any functions that start with "math." - that's your clue!
import math


def input_validator(number):
    """
    Validate that the input is appropriate for square root calculation.
    
    Args:
        number (float): The number to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    # TODO 20: Fix this validation logic - what makes a number valid for square root?
    # HINT: This function should return True only if:
    #       1. The number is actually a number (int or float type) AND 
    #       2. The number is positive (greater than 0)
    # Currently it only checks if number > 0, but what if someone passes in a string?
    # You need: isinstance(number, (int, float)) and number > 0
    return number > 0  # This is incomplete - missing type check!


def guess_starter(number):
    """
    Generate an intelligent initial guess for Newton's method.
    
    Args:
        number (float): The number to find the square root of
        
    Returns:
        float: A reasonable initial guess
    """
    # TODO 21: Complete this function - what's a good starting guess?
    # HINT: Different ranges of numbers need different starting strategies:
    # - For number == 1.0: return 1.0 (already done)
    # - For number < 1.0: return the number itself (good for small numbers like 0.25)
    # - For number > 1.0: return number / 2.0 (reasonable middle ground for larger numbers)
    # 
    # Use elif and else statements to handle all three cases!
    if number == 1.0:
        return 1.0
    # TODO: Add the other cases (number < 1 and number > 1)
    # elif number < 1.0:
    #     return number
    # else:
    #     return number / 2.0
    else:
        # This is incomplete - students need to add logic for other cases
        pass


def newton_iteration(number, current_guess):
    """
    Perform a single iteration of Newton's method.
    
    Args:
        number (float): The number to find the square root of
        current_guess (float): The current approximation
        
    Returns:
        float: The improved approximation
    """
    # TODO 22: Fix Newton's formula - there's a mathematical error below!
    # HINT: The Newton's method formula for square roots is: x_new = (x_old + number/x_old) / 2
    # Look carefully at the current formula: (current_guess + number * current_guess) / 2.0
    # The problem is "number * current_guess" - it should be "number / current_guess"
    # We want to DIVIDE number by current_guess, not MULTIPLY!
    return (current_guess + number * current_guess) / 2.0  # BUG: Should be division, not multiplication!


def has_converged(number, current_guess, tolerance):
    """
    Check if the current approximation has converged within the tolerance.
    
    Args:
        number (float): The target number
        current_guess (float): Current approximation
        tolerance (float): Acceptable error threshold
        
    Returns:
        bool: True if converged, False otherwise
    """
    # TODO 23: Complete the convergence check logic
    # HINT: We want to check if our guess is "close enough" to the correct answer.
    # The error calculation is already done: error = abs(current_guess * current_guess - number)
    # Now you need to compare this error to the tolerance.
    # Return True if error < tolerance (meaning we're close enough)
    # Return False otherwise
    error = abs(current_guess * current_guess - number)
    # TODO: Add the comparison with tolerance and return the result
    # The line should be: return error < tolerance


def display_iteration(iteration, guess, error):
    """
    Display the current iteration information.
    
    Args:
        iteration (int): Current iteration number
        guess (float): Current approximation
        error (float): Current error
    """
    print(f"Iteration {iteration:2d}: x = {guess:.8f}, error = {error:.2e}")


def newton_sqrt_calculator(number, tolerance=1e-6, max_iterations=100, initial=None, show_steps=False):
    """
    Calculate square root using Newton's method with while loops and conditionals.
    
    Args:
        number (float): The number to find the square root of
        tolerance (float): Convergence tolerance (default 1e-6)
        max_iterations (int): Maximum number of iterations (default 100)
        initial (float): Initial guess (if None, will be calculated)
        show_steps (bool): Whether to display iteration steps
        
    Returns:
        tuple: (result, iterations, converged)
    """
    # TODO 24: Fix the function call - use the corrected function name
    # HINT: Look at the function defined above - it's called 'input_validator', not 'validate_input'
    if not input_validator(number):
        raise ValueError("Input must be a positive number")
    
    # Handle special cases
    if number == 0:
        return 0.0, 0, True
    if number == 1:
        return 1.0, 0, True
    
    # Set initial guess
    if initial is None:
        # TODO 25: Fix this function call too
        # HINT: The function is called 'guess_starter', not 'initial_guess'
        current_guess = guess_starter(number)
    else:
        current_guess = float(initial)
    
    # Avoid division by zero
    if current_guess == 0:
        current_guess = 1.0
    
    iteration = 0
    converged = False
    
    # TODO 26: Write the main Newton's method loop
    # HINT: You need a while loop that continues while BOTH conditions are true:
    #       - iteration < max_iterations (to prevent infinite loops)
    #       - not converged (to stop when we're accurate enough)
    # 
    # Here's the structure you need to fill in:
    # while iteration < max_iterations and not converged:
    #     iteration += 1
    #     
    #     # Calculate error for display
    #     error = abs(current_guess * current_guess - number)
    #     
    #     # Show current iteration if requested
    #     if show_steps:
    #         display_iteration(iteration, current_guess, error)
    #     
    #     # Check if we've converged
    #     if has_converged(number, current_guess, tolerance):
    #         converged = True
    #         break
    #     
    #     # Get better approximation using Newton's method
    #     current_guess = newton_iteration(number, current_guess)
    
    # TODO: Students need to write the while loop here
    
    return current_guess, iteration, converged


def calculate_error_metrics(number, approximation):
    """
    Calculate various error metrics for the approximation.
    
    Args:
        number (float): Original number
        approximation (float): Calculated approximation
        
    Returns:
        dict: Dictionary containing error metrics
    """
    true_sqrt = math.sqrt(number)
    absolute_error = abs(approximation - true_sqrt)
    relative_error = absolute_error / true_sqrt if true_sqrt != 0 else 0
    squared_error = (approximation * approximation - number)
    
    # TODO 27: Create and return a dictionary with all these error metrics
    # HINT: You need to create a dictionary with these keys and their corresponding values:
    # Keys: 'absolute_error', 'relative_error', 'relative_error_percent', 'squared_error', 'true_value'
    # The values are the variables calculated above. Note that 'relative_error_percent' 
    # should be relative_error * 100 to convert to percentage.
    error_dict = {
        'absolute_error': absolute_error,
        'relative_error': relative_error,
        # TODO: Add the remaining keys and values:
        # 'relative_error_percent': relative_error * 100,
        # 'squared_error': squared_error,
        # 'true_value': true_sqrt
    }
    
    return error_dict


# Simplified version for students - removing complex functions
def display_iteration(iteration, guess, error):
    """
    Display the current iteration information.
    
    Args:
        iteration (int): Current iteration number
        guess (float): Current approximation  
        error (float): Current error
    """
    # Print iteration information to help with debugging
    print(f"Iteration {iteration:2d}: x = {guess:.8f}, error = {error:.2e}")