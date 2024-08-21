class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.score = 0
        self.queue = collections.deque([(0,0)])
        self.height = height
        self.width = width
        self.food= food
    def move(self, direction: str) -> int:
        head =  self.queue[-1] #pick righmost (head) of the queue without deleting it
        head_r = head[0]  
        head_c= head[1]
        if direction == 'U':
            head_r-=1
        elif direction == 'D':
            head_r+=1
        elif direction == 'L':
            head_c-=1
        elif direction == 'R':
            head_c+=1
        
        if head_r <0 or head_r > self.height-1 or head_c<0 or head_c >self.width-1:
            return -1
        #if self.food:
            # self.curfood = self.food[0]
        if self.food and [head_r , head_c] == self.food[0]:  #self.curfood[0] == head_r and self.curfood[1] ==head_c:
            self.queue.append([head_r, head_c])
            self.food.pop(0) #when food is eaten remove it. Always current food will be self.food[0]
            self.score+=1
        else:
            self.queue.popleft()
            if [head_r, head_c] in self.queue:
                return -1
            else:
             self.queue.append([head_r, head_c])

           return self.score
        
# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
