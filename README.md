# Abstraction in 3D Shape Modeling (Python OOP Project)

This project demonstrates the use of **abstraction**, **inheritance**, and **polymorphism** in Python by modeling various 3D shapes. Each shape calculates its surface area and volume using an abstract base class and random shape generation.

---

## Objective

- Create an abstract base class `Shape3D` with abstract methods for surface area and volume.
- Implement concrete classes: `Sphere`, `Cylinder`, and `Cube`.
- Use random generation to create and work with 3D shape objects.
- Demonstrate polymorphism through a common interface.

---

## 🧠 Concepts Demonstrated

- **Abstraction** using Python's `abc` module
- **Inheritance** to extend abstract base class
- **Randomization** with the `random` module
- **Math operations** using geometry formulas
- **Polymorphism** by calling methods through the same interface

---

## File Structure

## 2.Run the program:
python main.py


## Example Output
Sphere (radius=3)
  Surface Area: 113.10
  Volume: 113.10

Cube (side=7)
  Surface Area: 294.00
  Volume: 343.00

Cylinder (radius=6, height=16)
  Surface Area: 829.38
  Volume: 1809.56

 Class Descriptions
 Shape3D (abstract class)
surface_area() → returns the surface area

volume() → returns the volume

#Sphere
Formula:

Surface Area = 4πr²

Volume = (4/3)πr³

#Cylinder
Formula:

Surface Area = 2πr(r + h)

Volume = πr²h

#Cube
Formula:

Surface Area = 6a²

Volume = a³


![Снимок экрана (28)](https://github.com/user-attachments/assets/c6b5aebc-650c-431b-8a02-464317ef8106)





