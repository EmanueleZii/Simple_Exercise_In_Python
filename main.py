def greet_with(name = "", location=""):
    print("Hello,", name + "! How is the weather in", location + "?")

def main():
    greet_with(name="World", location="Wonderland")

if __name__ == "__main__":
    main()
