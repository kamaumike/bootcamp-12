class BinarySearch(list):
  """The Binary Search class
  """
  
  def __init__(self, a, b, *args):
    """Initialize the BinarySearch class
    """
    
    # Initialize the list object
    list.__init__(self, *args)
    
    self.length = a
    self.step = b
    
    # Value that determines upper bound for looping a list
    upper_bound = self.length * self.step 
    
    # Loop through all the numbers 
    for i in range(self.step, upper_bound + 1, self.step):
      self.append(i)
  
  def number_of_elements(self):
    """Returns the length of the list
    """
    return len(self.length)
  
  def search(self, value, start=0, stop=None, count=0):
    """Searches a value and returns a dictionary
    """
    
    # Check if the stop argument is empty
    if not stop:
      stop = self.length - 1
    # Check if the searched value is in the first index 
    if value == self[start]:
      return dict(count = count, index = start)
    # Check if the value argument has been entered 
    elif value == self[stop]:
      return dict(count = count, index = stop)
    
    # Divide the list into two and search
    middle = (start + stop) // 2
    
    # Check if the searched argument is in the middle index
    if value == self[middle]:
      return dict(count = count, index = middle)
    # Check if the searched argument is in the first part of the list
    elif value < self[middle]:
      stop = middle - 1
    # Check if the searched argument is in the second part of the list
    elif value > self[middle]:
      start = middle + 1
    
    if start >= stop:
      return dict(count = count, index = -1)
    # Add one everytime the search function iterates  
    count += 1  
    # Call the search function
    return self.search(value, start, stop, count)
