# A function to reverse a string without using [::-1] or built-in methods
def reverse_string(s):
# an empty string to make the reversed result
  reversed_string= ''
#a for- loop that iterates each character before reversing
for char in s :
# prepending the character to reverse the string
  reversed_string = char + reversed_string
return reversed_string # returns the reversed string
