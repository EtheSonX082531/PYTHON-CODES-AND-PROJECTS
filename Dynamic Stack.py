stack = []
Top = -1

def push():
    global Top
    x = int(input("Enter the Element: "))
    stack.append(x)
    Top += 1
    print(f"{x} pushed successfully.")

def pop():
    global Top
    if Top == -1:
        print("No Elements Available For Pop!")
    else:
        popped = stack.pop()
        Top -= 1
        print(f"Popped element: {popped}")

def top():
    if Top == -1:
        print("Stack is empty!")
    else:
        print(f"Top element is ---> {stack[Top]}")

def isEmpty():
    if Top == -1:
        print("Stack is empty.")
        return True
    else:
        print("Stack is not empty.")
        return False

def printStack():
    if Top == -1:
        print("Stack has no element to print!")
    else:
        print("Stack elements:", stack)

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek/Top")
    print("4. isEmpty")
    print("5. Print Stack")
    print("0. Exit")

    n = int(input("Enter Operation: "))

    if n == 0:
        print("Exiting...")
        break
    elif n == 1:
        push()
    elif n == 2:
        pop()
    elif n == 3:
        top()
    elif n == 4:
        isEmpty()
    elif n == 5:
        printStack()
    else:
        print("Invalid option!Try again.")
