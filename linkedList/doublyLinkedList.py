class Node:
    def __init__(self,data):
        self.data = data
        self.next= None
        self.prev = None


n1 = Node(10) 
n2 = Node(15)    
n3 = Node(20)  
n4 = Node(25)   
n5 = Node(30)   
n6 = Node(35)   
n7 = Node(40)   
n8 = Node(45)   
n9 = Node(50)


n1.next = n2

n2.prev = n1
n2.next = n3

n3.prev = n2
n3.next = n4

n4.prev = n3
n4.next = n5

n5.prev = n4
n5.next = n6


n6.prev = n5
n6.next = n7

n7.prev = n6
n7.next = n8

n8.prev = n7
n8.next = n9

n9.prev= n8
n9.next = n1


currentNode = n1
while currentNode:
    print(currentNode.data,end=" -> ")
    currentNode = currentNode.next
print("Null")    


print("backward")

lastNode = n9

while lastNode:
    print(lastNode.data,end=" -> ")
    lastNode = lastNode.prev
print("Null")




       