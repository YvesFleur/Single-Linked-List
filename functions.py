# create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create a list with nodes
class SingleLinkedList:
    def __init__(self):
        self.phead = None
        
    def checkLength(self):

        '''find out how many nodes there are in a given list'''

        p = self.phead
        if p is None:   
            # p is None means phead has no data, which means there is no node in the list
            return 0
        
        if p.next is None:
            # p.next is None means phead has data, but the next one does not
            # which means there is only 1 node
            return 1
        
        length = 0
        while p is not None:
            length += 1 
            p = p.next
            # the loop will break itself, then p is the last node
        return length
    
    # basic operations
    def insertFirst(self, x):   

        '''insert x as the first position of the list'''

        # create a new node with data=x and next=None
        new_node = Node(x)

        # check if the list already has element(s) or not
        length = self.checkLength()
        if length > 0:
            new_node.next = self.phead  
            # to store information of the next node into new_node

        self.phead = new_node

    def insertAfter(self, x, y):
        
        '''insert data x after node containing data y'''

        y_exist = self.search(y)
        # case 1: there is no y in the list
        if y_exist is None:
            print(f'{y} does not exist')
            return # to end the function
        
        # case 2: y is the last node
        if y_exist.next is None:
            self.insertLast(x)
        else:   
            # case 3: y is a random node except the last one 
            new_node = Node(x)
            new_node.next = y_exist.next    # to store information of the original next node of y
            y_exist.next = new_node     # to insert new_node (x) after y_exist (y)
            
    def insertLast(self, x):

        '''insert a new node as the last node'''

        length = self.checkLength()
        # case 1: the given list is Null, can not insert a node as the last node
        if length == 0:
            print('The given list is Null')
            return
        
        # case 2
        new_node = Node(x)
        p = self.phead
        while p.next != None:
            p = p.next
            # the loop will end itself, then p.next = None, 
            # which means p is the last node
        p.next = new_node   # insert new_node after p

    def deleteFirst(self):

        '''delete the first node'''

        self.phead = self.phead.next

    def search(self, x):

        '''return the searched node if exist'''

        length = self.checkLength()
        if length == 0:
            print('The given list is Null')
            return 
        
        p = self.phead
        while p != None:
            if p.data == x:
                return p
            p = p.next

    def sortAsc(self):
        length = self.checkLength()
        if length == 0:
            print('The given list is Null')
            return
        
        i = self.phead
        while i.next != None:
            j = i.next
            while j != None:
                if i.data > j.data:
                    i.data, j.data = j.data, i.data
                j = j.next
            i = i.next

    def sortDesc(self):
        length = self.checkLength()
        if length == 0:
            print('The given list is Null')
            return
        
        i = self.phead
        while i.next != None:
            j = i.next
            while j != None:
                if i.data < j.data:
                    i.data, j.data = j.data, i.data
                j = j.next
            i = i.next

    def showList(self):
        length = self.checkLength()
        if length == 0:
            print('The given list is Null')
            return
        
        p = self.phead
        while p is not None:
            print(p.data, end=' ', sep='\n')
            p = p.next

def insertList(list):

    '''insert a single linked list'''

    action = 1
    while action == 1:
        x = input('\nInsert value: ')
        list.insertFirst(x)
        action = int(input('Press 1 to insert another value or 0 to quit: '))
        if action == 0:
            break




        


    
            
