Stack = [-1] * 8
TopOfStack = -1

def Push(Item):
    global TopOfStack
    if TopOfStack == len(Stack) - 1:
        print("Stack is full")
        return False
    TopOfStack += 1
    Stack[TopOfStack] = Item
    return True

def Pop():
    global TopOfStack
    if TopOfStack == -1:
        print("Stack is empty")
        return -1
    item = Stack[TopOfStack]
    TopOfStack -= 1
    return item

def ShowStack():
    if TopOfStack == -1:
        return ""
    items = []
    for i in range(TopOfStack, -1, -1):
        items.append(str(Stack[i]))
    return " ".join(items)

def DecimalToBinary(Number):
    global TopOfStack
    TopOfStack = -1
    if Number == 0:
        return "0"
    while Number > 0:
        Push(Number % 2)
        Number //= 2
    result = ""
    while TopOfStack != -1:
        result += str(Pop())
    return result

def Editor(Commands):
    global TopOfStack
    TopOfStack = -1
    for cmd in Commands:
        if cmd.startswith("type "):
            Push(cmd[5:])
        elif cmd == "undo":
            Pop()
    result = ""
    for i in range(TopOfStack + 1):
        result += str(Stack[i])
    return result
