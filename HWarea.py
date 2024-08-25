import math

def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius ** 2

def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle given its length and width."""
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")
    return length * width

def calculate_triangle_area(base, height):
    """Calculate the area of a triangle given its base and height."""
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative.")
    return 0.5 * base * height

def main():
    while True:
        print("\nArea Calculator")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Exit")
        
        choice = input("Choose a shape (1-4): ")
        
        try:
            if choice == '1':
                radius = float(input("Enter the radius of the circle: "))
                area = calculate_circle_area(radius)
                print(f"The area of the circle with radius {radius} is: {area:.2f}")

            elif choice == '2':
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                area = calculate_rectangle_area(length, width)
                print(f"The area of the rectangle is: {area:.2f}")

            elif choice == '3':
                base = float(input("Enter the base of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                area = calculate_triangle_area(base, height)
                print(f"The area of the triangle is: {area:.2f}")

            elif choice == '4':
                print("Exiting the program. Goodbye!")
                break

            else:
                print("Invalid choice. Please select a number between 1 and 4.")

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()