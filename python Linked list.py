class Node:
    def __init__(self,current=None,nextNode=None):
        self.current = current
        self.nextNode = nextNode
        
        


class LinkedList:
    def __init__(self):
        self.head = None
        
        
    
    def insert(self,item):
        newNode = Node(item)
        
        if self.head == None:
            self.head = newNode
        else:
            currNode = self.head
            
            while(currNode.nextNode != None):
                currNode = currNode.nextNode
                
            currNode.nextNode = newNode
            
            
            
            
            
     
    def readNodes(self):
        
        curr = self.head
        List = []
        while(curr != None):
            
            List.append(curr.current)
            curr = curr.nextNode
        
        return List
            
l=LinkedList()

l.insert(1)
l.insert(2)
l.insert(4)
l.insert(5)
l.insert(6)

allitems = l.readNodes()

print(allitems)
            