# geometry.py content (simulate module in one file)
def circle_area(r):
    return 3.14159 * r ** 2

def circle_circumference(r):
    return 2 * 3.14159 * r

def rectangle_area(w, h):
    return w * h

def rectangle_perimeter(w, h):
    return 2 * (w + h)

# main.py content (test the "module")
if __name__ == "__main__":
    r = float(input("Enter circle radius: "))
    print(f"Area: {circle_area(r):.2f}")
    print(f"Circumference: {circle_circumference(r):.2f}")
    
    w = float(input("Enter rectangle width: "))
    h = float(input("Enter rectangle height: "))
    print(f"Area: {rectangle_area(w, h):.2f}")
    print(f"Perimeter: {rectangle_perimeter(w, h):.2f}")
