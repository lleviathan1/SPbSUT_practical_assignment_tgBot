import os
import sys

def main():
    for param in sys.argv:
        if param == "test":
            os.system("python3 tests.py")
            return 0
    os.system("python3 main.py")


if __name__ == "__main__":
    main()
