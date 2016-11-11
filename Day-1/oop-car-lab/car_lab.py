class Car(object):
  """The Car class that will be used 
  to instantiate various vehicles
  """
 
  num_of_doors = 4
  num_of_wheels = 4
  speed = 0
  
  def __init__(self, name='General', model='GM', type_of_car='saloon'):
    """Initialize the Car class"""
    
    self.name = name
    self.model = model
    self.type_of_car = type_of_car
    
    # Ensure the car has 2 doors if it's a Porshe or Koenigsegg
    if self.name == 'Porshe' or self.name == 'Koenigsegg':
      self.num_of_doors = 2
    # Ensure the car has 8 doors if it's a trailer
    elif self.type_of_car == 'trailer':
      self.num_of_wheels = 8
    else:
      # Ensure the car has 4 doors
      self.num_of_doors
    
  def drive(self, speed):
    """Checks the speed of the car"""
    
    # Multiply the speed of the trailer by 11
    if self.type_of_car == 'trailer':
      self.speed = speed * 11
    elif self.name == 'Mercedes':
      # Add the speed of the saloon by 997
      self.speed = speed + 997  
    return self

  def is_saloon(self):
    """Checks the type of car"""
    
    if self.type_of_car == 'saloon':
      return self.type_of_car
    elif self.type_of_car == 'trailer':
      self.type_of_car = 'trailer'
      return self.type_of_car
