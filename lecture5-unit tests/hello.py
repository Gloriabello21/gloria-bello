#ejemplo1
def main():
    name = input("what's your name? ")
    print(hello(name))

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "_main__":
    main()