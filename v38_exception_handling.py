# Types of Error
'''
>> Compiletime error
>> Logical error/Semantic error
>> Runtime error

'''
# compiletime error
'''Errors that occur during compilation are called Syntax errors'''
# Examples of syntax error
'''
print'hello'          # () is missing
d = 'delhi'
a = 2 + float(d)      # d is string, so it cannot be converted to float 
import math
a = math.pow(2)       # pow() needs two arguments
print(a)
'''

# Logical error
'''Error that are responsible for creating wrong results are called logical error or semantic errors.'''
# Examples 
'''program for adding two values'''
a = 10
b = 5
print(a-b)          # Here it prints the value 5 but the addition of 10 + 5 is 15.

# Execution  Error
'''if things go wrong during the execution is exceptions'''
try:
    # Code that may raise an exception
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    
    result = numerator / denominator
    
    # If the division is successful, print the result
    print("Result:", result)

except ValueError:
    # Handle the case when the user doesn't enter a valid integer
    print("Please enter valid integers for the numerator and denominator.")

except ZeroDivisionError:
    # Handle the case when the denominator is zero
    print("Error: Division by zero is not allowed.")

except Exception as e:
    # Handle any other unexpected exceptions
    print(f"An unexpected error occurred: {e}")

else:
    # This block is executed if no exception occurs
    print("Division operation successful.")

finally:
    # This block is always executed, regardless of whether an exception occurred
    print("Finally block executed.")
