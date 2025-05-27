"""This module contains the main application logic."""
def add(a, b):
    """This function does addition of two numbers."""
    return a + b

def subtract(a, b):
    """This function does subraction of two numbers."""
    return a - b

def multiply(a, b):
    """This function does multiplication of two numbers."""
    return a * b

def divide(a, b):
    """This function does division of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

print("Sum of 5 and 3 is:"+ str(add(5, 3)))
print("Difference of 5 and 3 is:"+ str(subtract(5, 3)))
print("Product of 5 and 3 is:"+ str(multiply(5, 3)))
print("Quotient of 5 and 3 is:"+ str(divide(5, 3)))
