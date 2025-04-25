# A function that computes factorial using loop
def factorial_using_loop(n):
 # initial value
  result = 1
 # for loop handling the increment of i
  for i in range(1, n+1):
    result = result * i
  return result # returns the final factorial
