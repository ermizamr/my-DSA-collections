class MinStack:

    def __init__(self):
        self.elements = []
        

    def push(self, val: int) -> None:
        if not self.elements:
            self.elements.append((val,val))
        else:
            current_min = self.elements[-1][1]
            self.elements.append((val,min(val,current_min)))

    def pop(self) -> None:
        self.elements.pop()

    def top(self) -> int:
        return self.elements[-1][0]
        

    def getMin(self) -> int:
        return self.elements[-1][1]
        
