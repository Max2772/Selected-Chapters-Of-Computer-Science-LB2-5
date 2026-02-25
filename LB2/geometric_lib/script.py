import os
import circle
import square

def main():
    a: float = float(os.environ.get('a', 0))
    r: float = float(os.environ.get('r', 0))

    print("Circle area:", circle.area(r))
    print("Circle perimeter", circle.perimeter(r))
    print("Square area:", square.area(a))
    print("Square perimeter:", square.perimeter(a))

if __name__ == "__main__":
    main()