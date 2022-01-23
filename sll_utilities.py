class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    def addFront(self, value):
        node1 = Node(value)
        node1.next = self.head
        self.head = node1
    def removeNode(self):
        if self.head == None:
            return None
        self.head = self.head.next
    def front(self):
        if self.head == None:
            return None
        else:
            return self.head.value
    def printSLL(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
    def contains(self, value):
        runner = self.head
        while runner != None:
            if runner.value == value:
                return True
            runner = runner.next
        return False
    def length(self):
        runner = self.head
        len_ct = 0
        while runner != None:
            len_ct+=1
            runner = runner.next
        return len_ct
    def display(self):
        runner=self.head
        display_str = ''
        while runner.next != None:
            display_str+=(str(runner.value)+", ")
            runner = runner.next
        display_str+=(str(runner.value))
        return display_str     

def moveMinFront(l_list):
    runner = l_list.head
    currMinNode = runner
    preMinNode = None
    while runner.next: 
        if runner.next.value < currMinNode.value:
            currMinNode = runner.next
            preMinNode = runner
        runner = runner.next
    if preMinNode: #in case the first value is the actual lowest value
        preMinNode.next = currMinNode.next
    currMinNode.next = l_list.head
    l_list.head = currMinNode

    return l_list

def moveMaxBack(l_list):
    runner = l_list.head
    currMaxNode = runner
    preMaxNode = None
    tail = None
    while runner.next:
        if runner.next.value > currMaxNode.value:
            currMaxNode = runner.next
            preMaxNode = runner
        runner = runner.next

    if preMaxNode and currMaxNode.next != None:
        preMaxNode.next = currMaxNode.next
        currMaxNode.next = runner.next
        runner.next = currMaxNode
    tail = runner
    
    if currMaxNode.next:
        tail.next = currMaxNode
        l_list.head = currMaxNode.next
    currMaxNode.next = None
    
    return l_list

l_list1 = SLL()

l_list1.addFront(3)
l_list1.addFront(5)
l_list1.addFront(7)
l_list1.addFront(111)

l_list1 = moveMaxBack(l_list1)
l_list1.printSLL()