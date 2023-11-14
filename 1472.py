class ListNode:
    def __init__(self, val="", next=None, prev=None):
        self.val, self.next, self.prev = val, next, prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage, None, None)


    def visit(self, url: str) -> None:
        self.head.next = ListNode(url, None, self.head)
        self.head = self.head.next

    def back(self, steps: int) -> str:
        while self.head.prev and steps > 0:  
            steps -= 1
            self.head = self.head.prev
        return self.head.val

    def forward(self, steps: int) -> str:
        while self.head.next and steps > 0:
            steps -=1
            self.head = self.head.next
        return self.head.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)