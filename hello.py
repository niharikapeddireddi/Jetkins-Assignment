import sys

def hello(name="World", roll=""):
    return "Hello %s! Your roll number is %s." % (name, roll)

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    roll = sys.argv[2] if len(sys.argv) > 2 else ""
    print(hello(name, roll))
