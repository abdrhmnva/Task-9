import random
from shapes import Sphere, Cylinder, Cube

def generate_random_shape():
    shape_type = random.choice(['Sphere', 'Cylinder', 'Cube'])

    if shape_type == 'Sphere':
        radius = random.randint(1, 10)
        return Sphere(radius)
    elif shape_type == 'Cylinder':
        radius = random.randint(1, 10)
        height = random.randint(5, 20)
        return Cylinder(radius, height)
    elif shape_type == 'Cube':
        side = random.randint(1, 10)
        return Cube(side)

def main():
    shapes = [generate_random_shape() for _ in range(10)]

    for shape in shapes:
        print(f"{shape}")
        print(f"  Surface Area: {shape.surface_area():.2f}")
        print(f"  Volume: {shape.volume():.2f}\n")

if __name__ == "__main__":
    main()
