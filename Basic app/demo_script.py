import sys


def demo_func(name: str, age: int):
    return f"Hello {name}, your age is {age}"


if __name__ == "__main__":
    name = sys.argv[1]
    age = int(sys.argv[2])
    print(demo_func(name, age))
