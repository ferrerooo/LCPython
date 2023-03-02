class BrowserHistory:

    def __init__(self, homepage: str):
        self.arr = []
        self.arr.append(homepage)
        self.right = 0
        self.cur = 0
        

    def visit(self, url: str) -> None:
        
        if self.cur < len(self.arr)-1:
            self.arr[self.cur+1] = url
            self.cur += 1
            self.right = self.cur
        else:
            self.arr.append(url)
            self.cur = self.cur+1
            self.right = self.cur
        #print(f'url:{url}, cur:{self.cur}, right:{self.right}')

    def back(self, steps: int) -> str:
        #print(self.arr, f'steps:{steps}, cur:{self.cur}, right:{self.right}')

        newcur = max(0, self.cur-steps)
        self.cur = newcur
        return self.arr[self.cur]

    def forward(self, steps: int) -> str:
        newcur = min(self.right, self.cur+steps)
        self.cur = newcur
        return self.arr[self.cur]

