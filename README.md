# freeCodeCamp-Polygon-Area-Calculator

## Instructions:
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator

<br>

## Purpose
In this project you will use object oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle and inherit methods and attributes.

```python
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
```



<br>

## Preview:
<img src="https://github.com/iVuDang/freeCodeCamp-Budget-App/blob/main/budget%20preview.png" width=100% height=100%>

<br>

## Technologies: 
* Python

<br>

## Outcome :white_check_mark: :
| Website | Link | 
| ------------- | ------------- | 
| Replit demo | https://replit.com/@iVuDang/freeCodeCamp-Budget-App-v1#main.py | 

<br>

- - - -

## My Notes - stuff I learned:  
1) parameter.function()

    ```python 
        another_shape.get_area())
    ```

takes the parameter, and calls upon the function 
The parameter is passed through the function

    ```python 
        def get_area(self):
            return (self.width * self.height)
    ```


2) super()
* The super() function is used to give access to methods and properties of a parent or sibling class.
* The super() function returns an object that represents the parent class.

    ```python 
        class Parent:
        def __init__(self, txt):
            self.message = txt

        def printmessage(self):
            print(self.message)

        class Child(Parent):
        def __init__(self, txt):
            super().__init__(txt)

        x = Child("Hello, and welcome!")

        # Takes the Child class, and calls the function def printmessage(self) of Parent
        x.printmessage()
    ```


<br>

## Citations:
* super() method idea inspired from RobisonTorres, sfoteini. 
* https://www.w3schools.com/python/ref_func_super.asp#:~:text=The%20super()%20function%20is,that%20represents%20the%20parent%20class.






