# Exercises

## Object Oriented Programming

1. Write these classes with OOP and inheritance.

```
                --------------
                    Shape
                --------------
                /           \
        -----------     -------------
            Poly            Circle
        -----------     -------------
          |
    -----------
        Rect
    -----------

```

1. Shape
   - circ()
2. Poly
   1. sides: list
3. Circle
   1. r: float
4. Rect

```python
# constructor call
poly = Poly([2, 3, 8, 9])
poly.sides[0] = 2

circle = Circle(2)

rect = Rect([1, 2])

# function call
print(poly.circ())
print(rect.circ())
print(circle.circ())

# operator overloading
print(poly < circle)
```