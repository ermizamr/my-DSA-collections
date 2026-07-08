class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.elements = [0]*capacity


    def get(self, i: int) -> int:
        return self.elements[i]


    def set(self, i: int, n: int) -> None:
        self.elements[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.elements[self.size] = n
        self.size += 1

    def popback(self) -> int:
        popped_element = self.elements[self.size-1]
        self.size -= 1
        return popped_element
 

    def resize(self) -> None:
        self.capacity *= 2
        new_elements = [0]*self.capacity
        for i in range(self.size):
            new_elements[i] = self.elements[i]
        self.elements = new_elements


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
