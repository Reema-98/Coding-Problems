# Node class
class Node:
 
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
 
# Linked List class
class LinkedList:
   
    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None
    
    def pushBegin(self,newdata):
        new_node=Node(newdata)
        new_node.next=self.head
        self.head=new_node
    
    def insertAfter(self,prevNode,newdata,):
        if prevNode is None:
            print("Previous node must be in linked list")
            return
        new_node=Node(newdata)
        new_node.next=prevNode.next
        prevNode.next=new_node

    def appendEnd(self,newdata):
        new_node=Node(newdata)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next

        last.next=new_node

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
        print('')

if __name__ == "__main__":
    ll=LinkedList()
    ll.pushBegin(1)
    ll.pushBegin(4)
    ll.appendEnd(2)
    ll.insertAfter(ll.head,3)
    ll.printList()
        