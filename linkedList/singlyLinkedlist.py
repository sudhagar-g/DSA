
class Node:  # creating class for to create simple single linked list

    def __init__(self,data):   
        self.data = data         #creating variable for to  storing values 
        self.next = None          # this variable for to point next memory location it's juct link the next node

#creating object
n1 = Node(10)
n2 = Node(25)
n3 = Node(37) 
n4 = Node(21)
n5 = Node(100)


n1.next = n2   #linking the 1st node to next node
n2.next = n3
n3.next = n4
n4.next = n5
#n5.next = n1     ==>  # it will create infinity loop



currentNode = n1

while currentNode:
    print(currentNode.data,end=" -> ")
    currentNode = currentNode.next
print("null")