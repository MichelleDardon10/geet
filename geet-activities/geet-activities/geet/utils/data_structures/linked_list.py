'''
[Data Structure] Linked List implementation.
'''


class Node:
    '''
    Node object.

    Attributes:
        hash (str): commit's hash
        message (str): commit's message
        author (str): user's name
        email (str): user's email
        next (Node): pointer to next node in list

    ⬇ Your code starts here:
    '''
    def __init__(self, hash: str, message: str, author = None, email= None):
        self.hash = hash
        self.message = message
        self.author = author
        self.email = email
        self.next = None


    def __repr__(self):
        return '| HASH: {} | MESSAGE: {}'.format(self.hash, self.message)
    

    '''
    ⬆ Your code ends here.
    '''

class LinkedList:
    '''
    Linked List object.

    Attributes:
        start (Node): pointer to first node in list

    Methods:
        __init__(self)
        __iter__(self)
        traverse(self)
        insert_first(self, node) #insert_first
        insert_last(self, node) #insert_last + #insert_before
        remove(key)
        reverse(self)

    ⬇ Your code starts here:
    '''
    def __init__(self):
        self.start = None

    def __iter__(self):
        node = self.start

        while node is not None:
            yield node
            node = node.next


    def __repr__(self):
        nodes = ["START"]

        for node in self:
            nodes.append(node.hash)
            

        nodes.append("NIL")
        return " --> ".join(nodes)

    def traverse(self):
        '''
        Navigates every node in the list.

        Args:
            None

        Returns:
            None
        '''
        
        current_node = self.start

        while current_node is not None:
            print(current_node)
            current_node = current_node.next


    def traverse_iter(self):
        '''
        Iterates trough the list using the __iter__ method.

        Args:
            None

        Returns:
            None
        '''

        for current_node in self:
            print(current_node)


    def insert_first(self, new_node: Node):
        '''
        Inserts a node at the start of the linked list.

        Args:
            new_node (Node): node to be inserted

        Returns:
            None
        '''

        new_node.next = self.start
        self.start = new_node


    def insert_last(self, new_node: Node):
        '''
        Inserts a node at the end of the linked list.

        Args:
            new_node (Node): node to be inserted

        Returns:
            None
        '''

        if self.start is None:
            self.start = new_node

        else:
            current_node = self.start
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node


    def insert_before(self, reference_node: str, new_node: Node):
        '''
        Inserts a node before the position of the reference node given.

        Args:
            reference_node (str): value of node used as reference
            new_node (Node): node to be inserted

        Returns:
            None
        '''

        if self.start is None:
            print('Empty linked list...')
            return

        if self.start.hash == reference_node:
            return self.insert_first(new_node)

        previous_node = self.start

        for current_node in self:

            if current_node.hash == reference_node:
                previous_node.next = new_node
                new_node.next = current_node
                return
            
            previous_node = current_node

        print('Reference node {} not found in linked list...'.format(reference_node))


    def remove(self, reference_node: str):
        '''
        removes a node given a value reference.

        Args:
            reference_node (str): value of node used as reference
            
        Returns:
            None
        '''

        if self.start is None:
            print('Empty linked list...')
            return   

        if self.start.hash == reference_node:
            self.start = self.start.next
            return
        
        previous_node = self.start

        for current_node in self:

            if current_node.hash == reference_node:
                previous_node.next = current_node.next
                return

            previous_node = current_node

        print('Reference node {} not found in linked list...'.format(reference_node))


    def reverse(self):

        previous_node = None
        current_node = self.start

        while current_node is not None:
            next_node= current_node.next
            current_node.next= previous_node
            previous_node = current_node
            current_node = next_node

        self.start = previous_node

        return self
        
    '''
    ⬆ Your code ends here.
    '''

'''
TESTING AREA

new_node = Node("1", "Si furula")
new_node_2 = Node("2", "Vamos a ver")

new_LinkedList = LinkedList()
new_LinkedList.insert_first(new_node)
new_LinkedList.insert_last(new_node_2)

new_LinkedList.reverse()

print(new_LinkedList)
'''