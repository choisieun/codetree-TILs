class Node:
    def __init__(self, data):
        self.data = data
        self.next = Node
        self.prev = Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0

    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        
        if self.head != None:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = Node

        else:
            self.head = new_node
            self.tail = new_node
            new_node.prev = Node

        self.node_num += 1

    def push_back(self, new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail

        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None

        else:
            self.head = new_node
            self.tail = new_node
            new_node.next = None

        self.node_num += 1

    def pop_front(self):
        if self.head == None:
            print("List is empty")

        elif self.head.next == None:
            temp = self.haed

            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data

        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None

            self.node_num -= 1
            return temp.data

    def pop_back(self):
        if self.tail == None:
            print("List is empty")

        elif self.tail.prev == None:
            temp = self.tail

            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data

        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None

            self.node_num -= 1
            return temp.data

    def size(self):
        return self.node_num

    def empty(self):
        return self.node_num == 0

    def front(self):
        return self.head.data

    def back(self):
        return self.tail.data

def main():
    n = int(input())
    linkedList = DoublyLinkedList()

    for i in range(n):
        instruction = input()

        if instruction.find("push_front") != -1:
            _, a = instruction.split(" ")
            linkedList.push_front(a)

        elif instruction.find("push_back") != -1:
            _, a = instruction.split(" ")
            linkedList.push_back(a)

        elif instruction == "pop_front":
            print(linkedList.pop_front())

        elif instruction == "pop_back":
            print(linkedList.pop_back())

        elif instruction == "size":
            print(linkedList.size())

        elif instruction == "empty":
            print(1) if linkedList.empty() else print(0)

        elif instruction == "front":
            print(linkedList.front())

        elif instruction == "back":
            print(linkedList.back())

if __name__ == '__main__':
    main()