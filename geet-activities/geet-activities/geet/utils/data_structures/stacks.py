class Stack: 
    
    '''
    Used to represent a PR
    
    
    
    '''

    def __init__(self, size: int):
        self.elements = [None] * size
        self.top = -1

    
    def __repr__(self):
        return 'Current stack: {} | Top: {}'.format(self.elements, self.top)


    def push(self, value: str) -> None:
        if self.top == len(self.elements) - 1:
            raise Exception('Stack overflow')

        self.top += 1
        self.elements[self.top] = value

    def pop(self) -> str:
        if self.top == -1:
            raise Exception('Stack underflow')
        
        value = self.elements[self.top]
        self.elements[self.top] = None # (Optional)
        self.top -= 1
        return value
    
    def peek(self) -> str:
        if self.top == -1:
            return 'Stack is empty'
        
        value = self.elements[self.top]
        return value