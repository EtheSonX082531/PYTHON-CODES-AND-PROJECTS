front = -1
rear = -1

def isFull():
    global rear, size
    if (rear == size - 1):
        print("Queue Full!")
        return True
    else:
        print("Queue is Not Full!")
        return False    

def head():
    global front
    return front

def tail():
    global rear
    return rear

def enqueue():
    global front, rear, size, queue
    if rear != size - 1:
        n = int(input("Enter Element: "))
        if front == -1 and rear == -1:
            front = 0
            rear = 0
            queue[rear] = n
        else:
            rear += 1
            queue[rear] = n
    else:
        print("Queue Overflow!")

def dequeue():
    global front, rear, queue
    if front == -1 or front > rear:
        print("No Element to Delete!")
    else:
        print(f"Deleted element from queue: {queue[front]}")
        queue[front] = None
        front += 1
        if front > rear:
            front = rear = -1 

def isEmpty():
    global front, rear
    if front == -1:
        print("Queue is Empty!")
        return True
    else:
        print("Queue is Not Empty!")
        return False

size = int(input("Enter Queue Size: "))
queue = [None] * size

while True:
    print("\n--- QUEUE ---")
    print("1. enqueue()")
    print("2. dequeue()")
    print("3. front()/head()")
    print("4. rear()/tail()")
    print("5. isFull()")
    print("6. isEmpty()")
    print("7. Show Queue")
    print("0. Exit()")
    
    n = int(input("Enter Operation: "))
    if n == 0:
        break
    elif n == 1:
        enqueue()
    elif n == 2:
        dequeue()
    elif n == 3:
        print(f"Front pointer: {head()}")
    elif n == 4:
        print(f"Rear pointer: {tail()}")
    elif n == 5:
        isFull()
    elif n == 6:
        isEmpty()
    elif n == 7:
        print(queue)
    else:
        print("Invalid option!")
