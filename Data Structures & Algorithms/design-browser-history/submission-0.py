class Node:
    def __init__(self, url):
        self.url = url
        self.previous = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):

        self.current = Node(homepage)
        
    def visit(self, url: str) -> None:
        
        new_node = Node(url)
        self.current.next = new_node
        new_node.previous = self.current
        self.current = new_node

    def back(self, steps: int) -> str:

        while steps > 0 and self.current.previous:
            self.current = self.current.previous
            steps -= 1
        return self.current.url
        

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)