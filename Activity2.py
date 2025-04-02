#!/usr/bin/env python
# coding: utf-8

# In[17]:


"""         Checks if a string is a palindrome (reads the same backward as forward). """
def is_palindrome(s):

   return s == s[::-1]

# Test case
string1 = "madam"
print(is_palindrome(string1)) 

string2 = "hello"
print(is_palindrome(string2))


# In[15]:


"""  This function takes a list of numbers and returns the largest number.  """
def find_largest(lst):
  if not lst:
      return None  # Return None for an empty list
  largest = lst[0]
  for number in lst:
      if number > largest:
          largest = number
  return largest

numbers = [10, 20, 5, 8, 25, 3]
print(find_largest(numbers))


# In[11]:


"""             This function counts the number of vowels (a, e, i, o, u) in a given string.         """
   def count_vowels(s):

   vowels = "aeiouAEIOU"
   count = 0
   for char in s:
       if char in vowels:
           count += 1
   return count
print(count_vowels("Hello World"))
print(count_vowels("Python"))  
print(count_vowels("Beautiful Day"))


# In[ ]:




