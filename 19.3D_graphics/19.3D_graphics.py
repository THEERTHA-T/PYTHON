from graphics import circle,rectangle
from graphics.dgraphics import cuboid,sphere

r=int(input("Enter the Radius of Circle :"))
circle.circle_area(r)
circle.circle_peri(r)

l=int(input("\nEnter the Length of Rectangle:"))
b=int(input("Enter the Breadth of Rectangle:"))
rectangle.rect_area(l,b)
rectangle.rect_peri(l,b)

l=int(input("\nEnter the Length of Cuboid:"))
b=int(input("Enter the Breadth of Cuboid :"))
h=int(input("Enter the Height of Cuboid:"))
cuboid.cuboid_area(l,b,h)
cuboid.cuboid_peri(l,b,h)

r=int(input("\nEnter the Radius of Sphere:"))
sphere.sphere_area(r)
sphere.sphere_peri(r)
