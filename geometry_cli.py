# calculate length and midpoint of a geometrical line segment
# include slope for 2D problems
# built by ChatGPT 1/1/24

import math

# Function definitions for calculations
def calculate_2d_slope(x1, y1, x2, y2):
    try:
        return (y2 - y1) / (x2 - x1)
    except ZeroDivisionError:
        return float('inf')

def calculate_midpoint(x1, y1, x2, y2, is_3d=False, z1=0, z2=0):
    if is_3d:
        return ((x1 + x2) / 2, (y1 + y2) / 2, (z1 + z2) / 2)
    else:
        return ((x1 + x2) / 2, (y1 + y2) / 2)

def calculate_length(x1, y1, x2, y2, is_3d=False, z1=0, z2=0):
    if is_3d:
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    else:
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_other_endpoint(x1, y1, xm, ym, is_3d=False, z1=0, zm=0):
    if is_3d:
        return (2*xm - x1, 2*ym - y1, 2*zm - z1)
    else:
        return (2*xm - x1, 2*ym - y1)

# Command line interface
def main():
    while True:
        print("\nWelcome to the Geometrical Line Segment Calculator")
        print("Press 'Q' at any time to quit.")

        user_input = input("Enter the dimension (2D/3D) or 'Q' to quit: ").strip()
        if user_input.upper() == 'Q':
            break

        is_3d = user_input.upper() == '3D'
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        z1 = float(input("Enter z1: ")) if is_3d else 0

        choice = input("Do you want to enter the second endpoint or midpoint? (E/M): ").strip().upper()
        if choice == 'Q':
            break
        elif choice == 'E':
            x2 = float(input("Enter x2: "))
            y2 = float(input("Enter y2: "))
            z2 = float(input("Enter z2: ")) if is_3d else 0
            midpoint = calculate_midpoint(x1, y1, x2, y2, is_3d, z1, z2)
            length = calculate_length(x1, y1, x2, y2, is_3d, z1, z2)
            print(f"Midpoint: {midpoint}")
            print(f"Length: {length}")
            if not is_3d:
                slope = calculate_2d_slope(x1, y1, x2, y2)
                print(f"Slope: {slope}")
        elif choice == 'M':
            xm = float(input("Enter xm: "))
            ym = float(input("Enter ym: "))
            zm = float(input("Enter zm: ")) if is_3d else 0
            other_endpoint = calculate_other_endpoint(x1, y1, xm, ym, is_3d, z1, zm)
            print(f"The other endpoint is: {other_endpoint}")

if __name__ == "__main__":
    main()

