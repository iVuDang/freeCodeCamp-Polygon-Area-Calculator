class Rectangle:
  # When a Rectangle object is created, it should be initialized with width and height attributes.
  def __init__(self, width, height):
    self.width = width
    self.height = height

# set_width
  def set_width(self, width):
    self.width = width

# set_height
  def set_height(self, height):
    self.height = height

# get_area: Returns area (width * height)
  def get_area(self):
    return (self.width * self.height)

# get_perimeter: Returns perimeter (2 * width + 2 * height)
  def get_perimeter(self):
    return ((2 * self.width) + (2 * self.height))

# get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)
  def get_diagonal(self):
    return (((self.width**2) + (self.height**2))**.5)

# get_picture: Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. There should be a new line (\n) at the end of each line.
# If the width or height is larger than 50, this should return the string: "Too big for picture.".
  def get_picture(self):
    if (self.width > 50 or self.height > 50):
      return "Too big for picture."
    else:
      row = (('*' * self.width) + '\n')
      shape = row * self.height
    return shape

# get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
  def get_amount_inside(self, another_shape):
    return (self.get_area() // another_shape.get_area())


# Additionally, if an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10)
  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

    
# Square class
class Square(Rectangle): 
  
# The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. 
# The __init__ method should store the side length in both the width and height attributes from the Rectangle class.
  def __init__ (self, length):
    super().__init__(length, length)
# If you give length to the square class, super() will store the length as the width and height back to the Rectangle parent class. 

# The Square class should be able to access the Rectangle class methods but should also contain a set_side method. If an instance of a Square is represented as a string, it should look like: Square(side=9)
  def set_side(self, side):
    self.width = side
    self.height = side
    
# Additionally, the set_width and set_height methods on the Square class should set both the width and height.

  def __str__(self):
    return f'Square(side={self.width})'


rect = Rectangle(10, 5)
print(rect.get_area())
# 50 

rect.set_height(3)
print(rect.get_perimeter())
# 26
print(rect)
# Rectangle(width=10, height=3)
print(rect.get_picture())
# **********
# **********
# **********


sq = Square(9)
print(sq.get_area())
# takes our square class and current parameter, and applies get_area function from our parent class
# 81 

sq.set_side(4)
# our set_side function accesses self.width, and self.height from our parent Rectangle class
# applies our new parameter of 4

print(sq.get_diagonal())
# takes our square class, and applies get_diagonal function from our parent class
# (((self.width**2) + (self.height**2))**.5)
# (16 + 16) ^ 0.5 or can rewritten as square root(32)
# x^(1/2) = √x
# 5.656854249492381

print(sq)
print(sq.get_picture())
# ****
# ****
# ****
# ****

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
# (self.get_area() // another_shape.get_area())

# self.get_area() = (self.width * self.height)  
# (8 * 16) = 128 

# another_shape.get_area()) = (self.width * self.height)  
# (4 * 4) = 16

# 128 // 16 = 8
# 8