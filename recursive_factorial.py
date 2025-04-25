# A function to calculate factorial using recursion
def recursive_factorial(i):
# Base case that prevents the function from calling itself 
  if i == 0 or i == 1:
    return 1
  # Recursive case if 'i' is greater than 1 
  else:
    return i * recursive_factorial(n-1)
