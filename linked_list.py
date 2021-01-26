class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return self.data
    
class Linked_List:
    def __init__(self):
        self.head = None
        
    #Insertation of the node at the begning. Time complexity(O(1))     
    def add_first(self,node):
        node.next = self.head
        self.head = node
        
    #Insertation of the node at the end. Time complexity(O(n))
    def add_end(self,node):
        n1 = self.head
        while n1.next is not None:
            n1 = n1.next
        n1.next = node    
        
    #Adding __iter__ () to traverse the LinkedlList using for loop..
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next    
        
    #Adding the __repr__() for more helpfull represetation of the object..    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next 
            
        nodes.append("None")
        return "->".join(nodes)
    
ll = Linked_List()
n1 = Node("a")
n2 = Node("b")
n3 = Node("c")
n4 = Node("d")

ll.head = n1 
n1.next = n2
n2.next = n3
n3.next = n4

ll.add_first(Node("0"))
ll.add_end(Node("e"))

print(ll) 
print()  
for i in ll:
    print(i)                     