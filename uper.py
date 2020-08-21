## when are we done with planning?
### if you can explain the problem simply
### ELI5
### good pseudocode
# code a factorial function
# first recursively, then iteratively
# U
## Clarify goal
### Calculate factorial of n
## might google, look up definition of factorial
## 5!
## 5 * 4 * 3 * 2 * 1
## 4! = 4 * 3 * 2 * 1
# 2! = 2
# 1! = 1
# 0! = 0 
# P
## recursive
### figure out the base case
### maybe 1, if number == 1 return number
### maybe 2, if number == 2 return 2
### how to approach the base
#### recurse with n - 1
### need to multiply the numbers
#### return n * funcname(n-1)
### how to account for 0?
# E
def recursive_factorial(n):
    if n < 0:
        return 0
    if n < 2:
        return 1
    return n * recursive_factorial(n - 1)
# print(recursive_factorial(5))
# print(recursive_factorial(2))
# print(recursive_factorial(1))
# print(recursive_factorial(0))
# Review
## negative numbers
## Handle non-integers
## Handle if return value >> Python's max value
### Used to be BigInt in Python
### now there is no upper bound
## Space and time complexity?
## Linear in time and space
# Iteratively
## U
## Plan
### Loop
#### For loop
#### while loop
### down to 1
### while we're not at 1
#### multiply total by the number
#### and decrement number
## E
def iterative_factorial(n):
    total = 1
    while n > 1:
        total *= n
        n -= 1
    return total
# print(iterative_factorial(5))
# print(iterative_factorial(2))
# print(iterative_factorial(0))
## run, right, fast
# Review
## Test with 0, 1, 2
## Space and time complexity?
### Linear time
### Constant space: O(1)
# Understand, Plan, Execute, Review
## "intuitive explanation of recursion"
### 3Blue1Brown
### BetterExplained
## Diagram
## Power!
## Write a function which given a number and an exponent, returns the number raised to that power
## don't use the built-in Python operator
## U
### multiply number by itself that many times
## 2**0.5
### what about if power is 0? --> 1
#   -What is a power
#   -What is an exponent
#   -What is a base
# Constrains (Dont use python operator)
## What about a negative base?
### flips between positive and negative
### in our function we have to wrap int in parens 
## What about a negative exponent?
### 2**(-2)
### 1/(2**2)
### 1/2 * 1/2
## P
### multiply int by itself recursively
### base case is 0
### if power is 0, return 1
## otherwise, recurse with exponent - 1
## return number times recursion result
## E
### multiply int by itself recursively
def recursive_power(base, exp):
### if power is 0, return 1
    if exp == 0:
        return 1
## if exp is 0, make whole thing a fraction
## change exp to positive
    if exp < 0:
        return 1/(base * recursive_power(base, -exp - 1))
## otherwise, recurse with exponent - 1
## return number times recursion result
    return base * recursive_power(base, exp - 1)
## Review
### Check basics
# print(recursive_power(2, 2))
# print(recursive_power(2, 3))
# ### Checked negative bases
# print(recursive_power(-2, 2))
# print(recursive_power(-2, 3))
# ### Check negative exp
# print(recursive_power(2, -2))
# should we handle all edge cases on first pass, in E?
## Run
# or wait until review?
## Right, fast
## law of complex systems?
### successful ones have evolved from simple systems
## Iterative version
## Understand
## Plan
#### before loop, check for 0 or negative exponents
#### Use exponent as counter
#### loop through multiplying the base
#### if neg exp, return as fraction
## Execute
def iterative_power(base, exp):
#### before loop, check for 0 or negative exponents
    total = 1
    counter = exp
    if exp == 0:
        return 1
    #### if neg exp, return as fraction
    elif exp < 0:
        counter = -counter
        base = 1/base
#### Use exponent as counter
    while counter > 0:
#### loop through multiplying the base
        total *= base
        counter -= 1
    return total
## Review
print(iterative_power(0, 0)) # 1
print(iterative_power(2, 0)) # 1
print(iterative_power(2, 2)) # 4
print(iterative_power(2, 3)) # 8
## negative bases
print(iterative_power(-2, 2))  # 4
print(iterative_power(-2, 3))  # -8
## negative exp
print(iterative_power(2, -2))  # 0.25
print(iterative_power(2, -3))  # 0.125 