class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None



def FindLowestVal(head):
    min_val = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < min_val:
            min_val = currentNode.data
        currentNode = currentNode.next
    return min_val    



n1 = Node(10) 
n2 = Node(15)    
n3 = Node(20)  
n4 = Node(25)   
n5 = Node(30)   
n6 = Node(35)   
n7 = Node(40)   
n8 = Node(45)   
n9 = Node(5 )


n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9

print(FindLowestVal(n1))