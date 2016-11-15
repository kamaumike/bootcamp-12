def reverse_string(string):
  """Returns the reverse of the string provided.
  """
  
  # Convert the string to lowercase
  lowercase = string.lower()
  # Initialize an empty string
  my_reversed_string = "" 

  # Check if the string is empty
  if len(lowercase) == 0:
    return None
  # Check if the string is a palindrome  
  elif lowercase == lowercase[::-1]:
    return True
  else:
    # Loop through the characters
    for i in lowercase:
      # Check if the string is not a palindrome 
      if lowercase != lowercase[::-1]:
        # Reverse the string
        my_reversed_string = lowercase[::-1]
        return my_reversed_string
