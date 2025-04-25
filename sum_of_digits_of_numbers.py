# A function that sums digits of a number
def sum_of_digits(i):
  #inital value
  total = 0
# a loop that ensures 'i' is greater than 0
while i > 0 :
  # adds the the last value of i to the total
  total= total + i % 10
  # removes the last digit from i
  i = i // 10
  return total # returns the sum of the digits
